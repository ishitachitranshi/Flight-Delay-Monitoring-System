import os
from io import BytesIO
from flask import Flask, render_template, request, send_file
import pandas as pd
import matplotlib
matplotlib.use("Agg")   # use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "flights.csv")
def load_data():
    try:
        df = pd.read_csv(DATA_PATH, low_memory=False)
        df.columns = df.columns.str.strip()
        # If YEAR/MONTH/DAY exist, create date column (safe)
        if all(c in df.columns for c in ("YEAR", "MONTH", "DAY")):
            try:
                df["FL_DATE"] = pd.to_datetime(df[["YEAR", "MONTH", "DAY"]])
            except Exception:
                pass
        # Create/normalize Total_Delay if possible
        delay_cols = [c for c in df.columns if "delay" in c.lower()]
        if "Total_Delay" not in df.columns and delay_cols:
            for c in delay_cols:
                df[c] = pd.to_numeric(df[c], errors="coerce")
            df["Total_Delay"] = df[delay_cols].sum(axis=1, min_count=1).fillna(0)
        return df
    except FileNotFoundError:
        return None

def guess_col(df, keywords):
    for k in keywords:
        for c in df.columns:
            if k.lower() in c.lower():
                return c
    return None

@app.route("/")
def index():
    df = load_data()
    if df is None:
        return "Error: flights.csv file not found. Please add the file to your project directory."

    head_html = df.head(12).to_html(classes="table table-sm table-striped", index=False)
    carrier_col = guess_col(df, ["carrier", "op_unique_carrier", "operator"])
    month_col = guess_col(df, ["month", "fl_date", "date"])
    carriers = sorted(df[carrier_col].dropna().unique().tolist()) if carrier_col else []
    months = sorted(pd.unique(df[month_col].dropna()).tolist()) if month_col else []
    return render_template("index.html",
                           head_html=head_html,
                           carriers=carriers,
                           months=months)

@app.route("/plot/<name>")
def plot_route(name):
    df = load_data()
    if df is None:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(0.5, 0.5, "Error: flights.csv not found.", ha="center", va="center")
        plt.tight_layout()
        buf = BytesIO()
        fig.savefig(buf, format="png")
        plt.close(fig)
        buf.seek(0)
        return send_file(buf, mimetype="image/png")

    # filters from querystring
    carrier = request.args.get("carrier", "All")
    month = request.args.get("month", "All")
    topn = int(request.args.get("topn", 10))
    # apply filters if possible
    carrier_col = guess_col(df, ["carrier", "op_unique_carrier", "operator"])
    month_col = guess_col(df, ["month", "fl_date", "date"])
    if carrier_col and carrier != "All":
        df = df[df[carrier_col] == carrier]
    if month_col and month != "All":
        # compare as string to be flexible
        df = df[df[month_col].astype(str) == str(month)]

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.set_style("whitegrid")

    if name == "top_airlines":
        if not carrier_col or "Total_Delay" not in df.columns:
            ax.text(0.5, 0.5, "Need a carrier column and Total_Delay.", ha="center", va="center")
        else:
            series = df.groupby(carrier_col)["Total_Delay"].mean().sort_values(ascending=False).head(topn)
            series.plot(kind="bar", ax=ax)
            ax.set_ylabel("Avg Total Delay (min)")
            ax.set_title("Top airlines by average delay")
            plt.xticks(rotation=45, ha="right")
    elif name == "cancelled_by_month":
        cancel_col = guess_col(df, ["cancel", "cancelled"])
        if not month_col or not cancel_col:
            ax.text(0.5, 0.5, "Need a month column and a cancelled column.", ha="center", va="center")
        else:
            series = df.groupby(df[month_col])[cancel_col].sum()
            series.plot(kind="bar", ax=ax)
            ax.set_ylabel("Cancelled flights")
            ax.set_title("Cancelled flights by month")
            plt.xticks(rotation=45)
    elif name == "monthly_heatmap":
        delay_cols = [c for c in df.columns if "delay" in c.lower()]
        if not month_col or not delay_cols:
            ax.text(0.5, 0.5, "Need a month column and at least one delay column.", ha="center", va="center")
        else:
            monthly = df.groupby(df[month_col])[delay_cols].mean()
            sns.heatmap(monthly, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
            ax.set_ylabel("Month")
    else:
        ax.text(0.5, 0.5, "Unknown plot requested", ha="center", va="center")

    plt.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

@app.route("/download")
def download_csv():
    return send_file(DATA_PATH, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # debug=True only for local testing; set False in production
    print("Attempting to run the Flask application...")
    app.run(host="0.0.0.0", port=port, debug=True)