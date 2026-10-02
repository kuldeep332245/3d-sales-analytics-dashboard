import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/sales_data.csv')

fig = px.scatter_3d(
df, x='Sales', y='Profit', z='Quantity',
color='Category', size='Quantity',
title='Sales vs Profit vs Quantity - 3D',
opacity=0.7
)

fig.update_layout(
template='plotly_dark',
height=700,
title_font_size=20
)

fig.write_html('../charts/scatter_chart.html')

print("3D Scatter Chart ban gaya!")
print("File: charts/scatter_chart.html")
