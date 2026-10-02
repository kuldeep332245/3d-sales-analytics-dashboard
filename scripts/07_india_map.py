import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/sales_data.csv')

state_sales = df.groupby('State')['Sales'].sum().reset_index()

fig = px.choropleth(
state_sales,
locations='State',
locationmode='country names',
color='Sales',
title='India State-wise Sales',
color_continuous_scale='Blues',
hover_name='State'
)

fig.update_geos(
fitbounds='locations',
visible=False,
showcountries=True,
countrycolor='#00D4FF',
showcoastlines=True,
coastlinecolor='#7B61FF',
showland=True,
landcolor='#1E2530'
)

fig.update_layout(
template='plotly_dark',
height=700,
title_font_size=20,
geo=dict(
scope='asia',
center=dict(lat=22, lon=78),
projection_scale=4
)
)

fig.write_html('../charts/india_map.html')

print("India Map ban gaya!")
print("File: charts/india_map.html")
