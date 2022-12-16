import pandas as pd
import seaborn as sns
import matplotlib.py as plt
import plotly.graph_objects as go
import plotly.express as px

dataset = pd.read_csv('projectC234_EPL.csv')

football_club = dataset['club'].value_counts().head(20)
print(football_club)

club = go.Figure(data = [go.Pie(labels = football_club.index,values = football_club.values, hole=0.5)])
club.show()