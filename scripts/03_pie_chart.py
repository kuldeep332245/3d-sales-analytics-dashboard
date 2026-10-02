import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/sales_data.csv')

cat = df.groupby('Category')['Sales'].sum().reset_index()

fig = px.pie(
cat, names='Category', values='Sales',
title='Category-wise Sales Share',
hole=0.4
)

fig.update_traces(
textposition='inside',
textinfo='percent+label',
marker=dict(line=dict(color='#0E1117', width=2))
)

fig.update_layout(
template='plotly_dark',
height=600,
title_font_size=20
)

fig.write_html('../charts/pie_chart.html')

print("3D Pie Chart ban gaya!")
print(cat)
