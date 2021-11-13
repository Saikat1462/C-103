import pandas as pd
import plotly.express as px

df=pd.read_csv("/WhiteHat Junior/Class 103/csv files/data.csv")
fig=px.bar(df,x="Country",y="InternetUsers")
fig.show()
