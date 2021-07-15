import numpy as np
import pickle

INF = int(1e9)
MAX = 105
class Node:
  ''' 
  Create the Node for Dijkstra's Input format
  
  Params:
  - id (num): the index of vertice
  - dis (num): weight of it
  '''
  def __init__(self, id, dis):
    self.id = id
    self.dis = dis
  def __lt__(self, other):
    return self.dis <= other.dis

class edge:
  ''' 
  Create edge for Bellman's Input format
  
  Params:
  - source (num): source vertice
  - target (num): target vertice
  - weight (num): the distance value from source to target
  '''
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight

def convert(data, destination=None, name=None):
  ''' 
  Convert Floyd Warshall's Input format to Bellman's, Dijkstra's Input format
  
  Params:
  ----
  data (dict): Floyd's Input  Format
  - destination: 2 option ['bellman','dijkstra'] to convert to the following format that you want
  - name (str): the name file that you wanna save as
  default: None when you don't want to save
  
  Return:
  dict format: the new format that's converted
  
  '''
  if destination == "dijkstra":
    new_dijsktra = {}
    dem = 0
    for vertices, gr in data.items():
      n = int(gr['v'])
      graph = [[] for _ in range(n+5)]
      dist = [INF for _ in range(n+5)]
      path = [-1 for _ in range(n+5)]
      dis = np.copy(gr['dis'])
      # path = gr['path']
      for i in range(dis.shape[0]):
        for j in range(dis.shape[1]):
          if dis[i][j] != 0 and dis[i][j]!= INF:
            graph[i].append(Node(j, dis[i,j]))
      new_dijsktra[str(dem)] = {'graph': graph, 'path': path, 'dis': dist, 'edge': gr['edge'], 'v': n}
      dem+=1
    if name !=None:  
      with open(name, 'wb') as f:
        pickle.dump(new_dijsktra, f)
    print("Done")
    return new_dijsktra

  elif destination == "bellman":
    new_bellman = {}
    dem = 0
    for vertices, gr in data.items():
      graph = []
      dist = [INF for _ in range(MAX)]
      path = [-1 for _ in range(MAX)]
      dis = gr['dis']
      for i in range(dis.shape[0]):
        for j in range(dis.shape[1]):
          if dis[i][j] != 0 and dis[i][j] != INF:
            graph.append(edge(i, j, dis[i][j]))
            # e+=1
      new_bellman[str(dem)] = {'graph': graph, 'path': path, 'dis': dist, 'edge': gr['edge'], 'v': int(gr['v'])}
      # print(e == gr['edge'])
      dem += 1
    if name != None:
      with open(name, 'wb') as f:
        pickle.dump(new_bellman, f)
    print('Done')
    return new_bellman