import pandas as pd
import json

df = pd.read_csv('../data/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

total_sales = int(df['Sales'].sum())
total_profit = int(df['Profit'].sum())
total_orders = len(df)
total_customers = df['Order_ID'].nunique()
avg_order_value = int(total_sales / total_orders)
profit_margin = round((total_profit / total_sales) * 100, 2)

df['Month'] = df['Date'].dt.to_period('M')
monthly = df.groupby('Month')['Sales'].sum()

growth = 0
if len(monthly) >= 2:
growth = round(((monthly.iloc[-1] - monthly.iloc[-2]) / monthly.iloc[-2]) * 100, 2)

kpi = {
'total_sales': total_sales,
'total_profit': total_profit,
'total_orders': total_orders,
'total_customers': total_customers,
'avg_order_value': avg_order_value,
'profit_margin': profit_margin,
'monthly_growth': growth
}

f = open('../data/kpi_summary.json', 'w')
json.dump(kpi, f, indent=2)
f.close()

print("=" * 50)
print("KPI SUMMARY - Dashboard Cards")
print("=" * 50)
print(f"Total Sales:      Rs {total_sales:,}")
print(f"Total Profit:     Rs {total_profit:,}")
print(f"Total Orders:     {total_orders:,}")
print(f"Total Customers:  {total_customers:,}")
print(f"Avg Order Value:  Rs {avg_order_value:,}")
print(f"Profit Margin:    {profit_margin}%")
print(f"Monthly Growth:   {growth}%")
print("=" * 50)
print("Saved: data/kpi_summary.json")
