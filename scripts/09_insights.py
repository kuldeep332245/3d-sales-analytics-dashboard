import pandas as pd

df = pd.read_csv('../data/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')

print("=" * 50)
print("SMART AUTO INSIGHTS - Sales Dashboard")
print("=" * 50)

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = len(df)
profit_margin = (total_profit / total_sales) * 100

print(f"\nTotal Sales: Rs {total_sales:,}")
print(f"Total Profit: Rs {total_profit:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Profit Margin: {profit_margin:.2f}%")

best_month = df.groupby('Month')['Sales'].sum().idxmax()
best_month_sales = df.groupby('Month')['Sales'].sum().max()
print(f"\nBest Month: {best_month} (Rs {best_month_sales:,})")

top_product = df.groupby('Product')['Sales'].sum().idxmax()
top_product_sales = df.groupby('Product')['Sales'].sum().max()
print(f"Top Product: {top_product} (Rs {top_product_sales:,})")

top_region = df.groupby('Region')['Sales'].sum().idxmax()
top_region_sales = df.groupby('Region')['Sales'].sum().max()
print(f"Top Region: {top_region} (Rs {top_region_sales:,})")

top_state = df.groupby('State')['Sales'].sum().idxmax()
top_state_sales = df.groupby('State')['Sales'].sum().max()
print(f"Top State: {top_state} (Rs {top_state_sales:,})")

best_payment = df.groupby('Payment_Mode')['Sales'].sum().idxmax()
print(f"Most Used Payment: {best_payment}")

avg_age = df['Customer_Age'].mean()
print(f"Average Customer Age: {avg_age:.1f} years")

print("\n" + "=" * 50)
print("Recommendations:")
print("=" * 50)
print(f"1. Focus more on {top_product} - best seller")
print(f"2. Expand in {top_region} region")
print(f"3. Promote {best_payment} payment mode")
print(f"4. Target age group: {int(avg_age)-5}-{int(avg_age)+5} years")
print("=" * 50)
