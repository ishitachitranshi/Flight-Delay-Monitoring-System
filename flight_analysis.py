import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid", font_scale=1.1)


df = pd.read_csv("flights.csv", dtype={'ORIGIN_AIRPORT': str, 'DESTINATION_AIRPORT': str}, low_memory=False)


df['FL_DATE'] = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY']])


df.rename(columns={
    'AIR_SYSTEM_DELAY': 'NAS_DELAY',
    'AIRLINE_DELAY': 'CARRIER_DELAY'
}, inplace=True)


delay_cols = ['CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY']
for col in delay_cols:
    if col not in df.columns:
        df[col] = 0
    else:
        df[col] = df[col].fillna(0)


df['CANCELLED'] = df['CANCELLED'].fillna(0)
df['OP_UNIQUE_CARRIER'] = df['AIRLINE'].fillna('UNKNOWN')


df['Month'] = df['FL_DATE'].dt.month
df['DayOfWeek'] = df['FL_DATE'].dt.dayofweek


df['Total_Delay'] = df[delay_cols].sum(axis=1)


plt.figure(figsize=(10, 5))
sns.barplot(x='Month', y='Total_Delay', data=df, estimator=sum, errorbar=None)
plt.title('Total Delay by Month')
plt.xlabel('Month')
plt.ylabel('Total Delay (minutes)')
plt.grid(True)
plt.tight_layout()
plt.show()

avg_delays = df[delay_cols].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
avg_delays.plot(kind='bar', color='skyblue')
plt.title("Average Delay by Cause")
plt.ylabel("Average Delay (minutes)")
plt.grid(axis='y')
plt.tight_layout()
plt.show()


monthly_delay = df.groupby('Month')[delay_cols].mean()
plt.figure(figsize=(10, 6))
sns.heatmap(monthly_delay, annot=True, fmt=".1f", cmap="YlGnBu")
plt.title("Monthly Average Delay by Cause")
plt.tight_layout()
plt.show()


top_airlines = df.groupby('OP_UNIQUE_CARRIER')['Total_Delay'].mean().sort_values(ascending=False).head(10)
top_airlines.plot(kind='bar', color='orange', figsize=(10, 5))
plt.title('Top 10 Airlines by Average Delay')
plt.ylabel('Average Total Delay (min)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


cancel_month = df.groupby('Month')['CANCELLED'].sum()
cancel_month.plot(kind='bar', color='red', figsize=(10, 5))
plt.title('Number of Cancelled Flights by Month')
plt.ylabel('Cancelled Flights')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

print("\n✅ Flight Delay Analysis completed successfully. All plots displayed.\n")
