import numpy as np

class Bellman(Floyd):
    ''' 
    Bellman algorithm
    '''
    def __init__(self, data):
        super().__init__(data)
    
    def bellman(self, s, dist, path, graph, n, m):
        ''' 
        
        '''
        dist[s] = 0
        size = 0
        for i in range(1, n):
            for j in range(m):
                u = graph[j].source
                v = graph[j].target
                w = graph[j].weight
                if dist[u]!=INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    path[v] = u
                    size += dist[v].__sizeof__() + path[v].__sizeof__()
        return path, size

    def findPath(self):
        for v, gr in self.data:
        
            graph, edge, v_ = np.copy(gr['graph']), gr['edge'], gr['v']
            self.V.append(v_)
            self.edge.append(edge)
            ends = 0
            sizes = 0
            for s in range(v_):
                path, dist = np.copy(gr['path']), np.copy(gr['dis'])
                start = time()
                path, size = self.bellman(s, dist, path,graph, v_, edge)
                end = time() - start
                ends += end
                sizes+=size
            
            self.times.append(ends)
            self.size.append(sizes)
        print(self.size)

if __name__ == "__main__":
  bellman = Bellman(graph_bellman)
  bellman.save('/content/data/bellman_ThucNghiem.csv')