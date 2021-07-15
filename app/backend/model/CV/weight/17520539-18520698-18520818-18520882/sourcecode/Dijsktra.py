from Floyd import Floyd

class Dijsktra(Floyd):
    
    def __init__(self, data=None):
        super().__init__(data)

    def dijkstra(self, s, graph, dist, path):
        pq = queue.PriorityQueue()
        pq.put(Node(s, 0))
        dist[s] = 0
        size = 0
        while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dis
        if dist[u] != w:
            continue
        for neighbor in graph[u]:
            if w + neighbor.dis < dist[neighbor.id]:
            dist[neighbor.id] = w + neighbor.dis
            pq.put(Node(neighbor.id, dist[neighbor.id]))
            path[neighbor.id] = u
            size += path[neighbor.id].__sizeof__() + dist[neighbor.id].__sizeof__()
        return path, size
    def findPath(self):
        # V, times = [], []
        for v, gr in self.data:
        
            graph, edge, v_ = np.copy(gr['graph']), np.copy(gr['edge']), np.copy(gr['v'])
            # v_ = v
            self.V.append(v_)
            self.edge.append(edge)
            ends = 0
            sizes = 0
            for s in range(v_):
                path, dist = np.copy(gr['path']), np.copy(gr['dis'])
                start = time()
                path, size = self.dijkstra(s, graph, dist, path)
                end = time() - start
                ends+=end
                sizes+=size
                # print('Dinh:', s)
                # for d in range(s):
                #   if d!=s:
                #     print(path[:v_])
                #     break
            # end = time() - start
            self.times.append(ends)
            self.size.append(sizes)
        print(self.size)

if __name__ == "__main__":
  graph = Dijsktra(graph_dijsktra)
  graph.save('data/dijsktra_ThucNghiem.csv')