import plotly.express as px
import pandas as pd

data = pd.DataFrame(
    {"City": ["Tokyo", "Delhi", "NYC", "Paris", "Cairo"], "Temp": [16, 32, 14, 12, 28]}
)
fig = px.bar(data, x="City", y="Temp", title="Average temperature by City")

fig.show()
