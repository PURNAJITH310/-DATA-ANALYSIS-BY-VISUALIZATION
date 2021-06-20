import pandas as pd
import csv 
import plotly_express as px
df=pd.read_csv("data.csv")
student=df.loc[df['student_id']=="TRL_zny"]
print(student.groupby("level")["attempt"].mean())
fig=px.bar(x=student.groupby("level")["attempt"].mean() ,y=["level1","level2","levwl3","level4"])
fig.show()