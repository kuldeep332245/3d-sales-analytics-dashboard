import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')

monthly = df.groupby('Month').agg(
Sales=('Sales', 'sum'),
Profit=('Profit', 'sum')
).reset_index()

month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthly['Month'] = pd.Categorical(monthly['Month'], categories=month_order, ordered=True)
monthly = monthly.sort_values('Month')

fig = px.line_3d(
monthly, x='Month', y='Sales', z='Profit',
title='Monthly Sales & Profit Trend - 3D',
markers=True
)

fig.update_traces(line=dict(width=6, color='#00D4FF'))

fig.update_layout(
template='plotly_dark',
height=700,
title_font_size=20
)

fig.write_html('../charts/line_chart.html')

print("3D Line Chart ban gaya!")
print("File: charts/line_chart.html")
