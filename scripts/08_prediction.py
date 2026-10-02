import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('../data/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')

monthly = df.groupby('Month')['Sales'].sum().reset_index()

month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthly['Month'] = pd.Categorical(monthly['Month'], categories=month_order, ordered=True)
monthly = monthly.sort_values('Month').reset_index(drop=True)

x = np.arange(len(monthly))
y = monthly['Sales'].values

n = len(x)
slope = (n * np.sum(x*y) - np.sum(x)*np.sum(y)) / (n * np.sum(x*x) - np.sum(x)**2)
intercept = (np.sum(y) - slope * np.sum(x)) / n

next_x = len(monthly)
prediction = slope * next_x + intercept

months_list = monthly['Month'].tolist() + ['Next']
sales_list = monthly['Sales'].tolist() + [prediction]

fig = px.bar(
x=months_list, y=sales_list,
title=f'Next Month Prediction: Rs {int(prediction):,}',
color=sales_list,
color_continuous_scale='Blues'
)

fig.update_layout(
template='plotly_dark',
height=600,
title_font_size=20,
xaxis_title='Month',
yaxis_title='Sales'
)

fig.write_html('../charts/prediction.html')

print("Prediction chart ban gaya!")
print(f"Next month expected sales: Rs {int(prediction):,}")
