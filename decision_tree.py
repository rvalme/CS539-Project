import pydotplus
from sklearn import tree
import collections
import pandas as pd
import os     
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# load data
dataset = pd.read_csv('2017_USCensus_Cleaned.csv', header=0)
# split data into X and y
X = dataset.drop(['Unnamed: 0', 'ZIP', 'Count'], axis=1)
Y = dataset.Count


print(X)
print(Y)

# Training
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

#tree = DecisionTreeClassifier().fit(X, y)
#tree.feature_importances_

feat_impt = (dict(zip(X, clf.feature_importances_)))
(pd.DataFrame.from_dict(data=feat_impt, orient='index')
   .to_csv('feature_importances.csv', header=False))

dot_data = tree.export_graphviz(clf,
                                out_file=None,
								feature_names=dataset.columns[2:56],
								max_depth=20,
                                filled=True,
                                rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)

colors = ('turquoise', 'orange')
edges = collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))

for edge in edges:
    edges[edge].sort()    
    for i in range(2):
        dest = graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])

graph.write_png('tree_final.png')


