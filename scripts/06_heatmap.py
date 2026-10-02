import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/sales_data.csv')

pivot = df.pivot_table(
values='Sales',
index='Region',
columns='Category',
aggfunc='sum'
).reset_index()

pivot_melted = pivot.melt(id_vars='Region', var_name='Category', value_name='Sales')

fig = px.density_heatmap(
pivot_melted,
x='Region', y='Category', z='Sales',
title='Region vs Category - Sales Heatmap',
color_continuous_scale='Viridis',
text_auto=True
)

fig.update_layout(
template='plotly_dark',
height=600,
title_font_size=20
)

fig.write_html('../charts/heatmap.html')

print("Heatmap ban gaya!")
print("File: charts/heatmap.html")
