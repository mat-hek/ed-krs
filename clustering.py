import networkx as nx
import pandas as pd
from pprint import pprint

df = pd.read_csv('csv/relations.csv')
tg = nx.from_pandas_edgelist(df, source='person_id', target='subject_id', create_using=nx.Graph())
g = nx.Graph()
for index, row in df.iterrows():
    pid = row['person_id']
    sid = row['subject_id']
    g.add_node(pid)
    for n in tg.neighbors(sid):
        g.add_edge(pid, n)

print(nx.average_clustering(g))
print(sum(nx.triangles(g).values())/3)
print(nx.transitivity(g))
