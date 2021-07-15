import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from time import time
import pickle
import json
import queue
np.set_printoptions(precision=33)

"""**Xay dung ham**

#Create dataset
"""

class Data:
  
  def __init__(self, time, name, v=12, t=1.09):
    # self.V = V
    self.v = v
    self.t = t
    self.INF = int(1e9)
    self.name = name
    # # self.path, self.dis = self.create()
    self.time = time
    self.graph = {}

  def create(self, V):
    INF = self.INF
    path = np.zeros((V,V))
    dis = np.zeros((V, V))
    Graph = np.random.randint(0, 10, size = (V,V))
    edge = 0
    #print(Graph)
    #dis = np.copy(Graph)
    # for i in range(V):
    #   for j in range(V):
    #     dis[i][j] = INF if i!=j and Graph[i][j]==0 else Graph[i][j]
    dis = np.where(Graph!=0, Graph, INF)
    #print(dis)
    for i in range(V):
      dis[i][i] = 0
      for j in range(V):
        if dis[i][j] != INF and i!=j:
          path[i][j] = i
          edge += 1
        else:
          path[i][j] = -1
    return path.astype(np.int) , dis.astype(np.int), edge

  def dataset(self):
    V = []
    v = self.v
    for i in range(self.time):
      V.append(v)
      path, dis, edge = self.create(v)
      # print(dis)
      # start = time()
      # dis, path = floyd(dis, v, path)
      # end = time() - start
      self.graph[str(i)] = {'path': path, 'dis': dis, 'edge': edge, 'v': v}
      # times.append(end)
      v*=self.t
      v = int(v)
    with open(self.name, 'wb') as f:
      pickle.dump(self.graph,f)

if __name__ == "__main__":
  data = Data(30, 'floyd_path.pkl')
  data.dataset()