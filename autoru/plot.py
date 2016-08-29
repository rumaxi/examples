import db
import plotly
from plotly.graph_objs import Scatter, Layout, Bar, Figure
from peewee import fn
from peewee import *


maximum={}
minimum={}
avg={}
tmp=[]

for year in list(reversed(range(2005,2015))):
    query = db.Auto.select().where(db.Auto.year == year)
    for res in query:
        tmp.append(res.price)
    maximum[year]=max(tmp)
    minimum[year]=min(tmp)
#    avg[year]=reduce(lambda x, y: x + y, tmp) / len(tmp)
    avg[year]=sum(tmp) / float(len(tmp))
    tmp=[]




trace1 = Bar(
    x=list(maximum.keys()),
    y=list(maximum.values()),
    name='Max'
)

trace2 = Bar(
    x=list(minimum.keys()),
    y=list(minimum.values()),
    name='Min'
)



trace3 = Bar(
    x=list(avg.keys()),
    y=list(avg.values()),
    name='Avg'
)

data = [trace1, trace2,trace3]
layout = Layout(
    barmode='group'
)
fig = Figure(data=data, layout=layout)
plot_url = plotly.offline.plot(fig, filename='stacked-bar')

