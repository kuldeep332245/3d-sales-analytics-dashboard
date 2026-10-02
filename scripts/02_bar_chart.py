import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')

monthly = df.groupby('Month')['Sales'].sum().reset_index()

month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthly['Month'] = pd.Categorical(monthly['Month'], categories=month_order, ordered=True)
monthly = monthly.sort_values('Month')

fig = px.bar(
monthly, x='Month', y='Sales',
title='Monthly Sales - 3D View',
color='Sales',
color_continuous_scale='Blues'
)

fig.update_layout(
template='plotly_dark',
height=600,
title_font_size=20
)

fig.write_html('../charts/bar_chart.html')

print("3D Bar Chart ban gaya!")
print("File: charts/bar_chart.html")
print(monthly)
