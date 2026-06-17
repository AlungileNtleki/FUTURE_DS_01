import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

print("loading data...")
df = pd.read_csv(
    r"C:\Users\Dell\Downloads\ga-customer-revenue-prediction\train.csv",
    nrows=50000
)
print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
print(df.head())
print(df.info())
print(df.shape)
def parse_col(col):
    return col.apply(lambda x: json.loads(x) if isinstance(x, str) else {})

totals_df = pd.json_normalize(parse_col(df['totals']))
device_df = pd.json_normalize(parse_col(df['device']))
traffic_df = pd.json_normalize(parse_col(df['trafficSource']))
clean = pd.DataFrame()
clean['channel'] = df['channelGrouping']
clean['device'] = device_df['deviceCategory']
clean['visits'] = pd.to_numeric(totals_df['visits'], errors='coerce').fillna(0)
clean['pageviews'] = pd.to_numeric(totals_df['pageviews'], errors='coerce').fillna(0)
clean['bounces'] = pd.to_numeric(totals_df['bounces'], errors='coerce').fillna(0)
clean['revenue'] = pd.to_numeric(totals_df['transactionRevenue'], errors='coerce').fillna(0)
clean['source'] = traffic_df['source']
clean['medium'] = traffic_df['medium']
clean['converted'] = (clean['revenue'] > 0).astype(int)

clean.to_csv('funnel_summary.csv', index=False)
print("CSV exported successfully!")
