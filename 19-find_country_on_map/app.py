import plotly.express as px

country = input("Enter the country name: ")
data = {"Country": [country], "Values": [100]}

fig = px.choropleth(
    data,
    locations="Country",
    locationmode="country names",
    color="Values",
    color_continuous_scale="Inferno",
    title=f"Country Map Highlighting {country}",
)

fig.show()
