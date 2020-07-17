import plotly.express as px 
import pandas as pd #pd = pandas 

# Dataframe - read the file 
df = pd.read_csv("austpop.csv")

# Line Graphs - directly correspond to fields of data 
fig = px.line(df, x="year", y="Aust", title="Australian Population")
# fig.show()

# Multiple lines on a grpah (different variables)
fig = px.line(
    df, 
    x="year", 
    y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
    title="Australian Population by State"
)
# fig.show()

# Line Graphs (dictionary, with lists as values)
df_a = {
    "our_data": [123, 132, 654, 345, 125, 498],
    "more_data": [345, 67, 176, 245, 197, 391],
    "columns": ["a", "b", "c", "d", "e", "f"]
}
fig = px.line(df_a, y="our_data", x="columns")
# fig.show()

# Scatterplots 
fig = px.scatter(
    df,
    x=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
    y="year"
)
# fig.show()

#Barchart 
fig = px.bar(df, x="year", y=["NSW"])
# fig.show()

fig = px.bar(
    df,
    x="year",
    y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
    barmode="group" #group by year 
)
fig.show()

