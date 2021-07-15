def createData(namefile='dijsktra_graph.pkl'):
      with open(namefile, 'rb+') as f:
    graph = pickle.load(f)
  return graph

if __name__ == "__main__":
  graph_floyd, graph_dijsktra, graph_bellman =createData(namefile='floyd_path.pkl'), createData(), createData(namefile='bellman_graph.pkl')