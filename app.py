import plotly.express as px
import pandas as pd

df = pd.read_csv('53253.csv')

fig = px.line(df, x="x", y="y", title="Unsorted Input")
fig.show()

df = df.sort_values(by="x")
fig = px.line(df, x="x", y="y", title="Sorted Input")
fig.show()
