class Floyd:
    def __init__(self, data):
    # self.V = V
        self.data = data.items()
        self.size, self.V, self.times, self.edge = [], [], [], []

    def floyd(self, dis, V, path):
        size = 0
        # print(dis)
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if dis[i][j] > dis[i][k] + dis[k][j]:
                        dis[i][j] = dis[i][k] + dis[k][j]
                        path[i][j] = path[k][j]
                        size += dis[i][j].__sizeof__() + path[i][j].__sizeof__() 
                    # print('OK')
            # size = dis.__sizeof__() + path.__sizeof__()    
        return dis, path, size

    def findPath(self):
        # V, times = [], []
        for i, gr in self.data:
        
            path, dis, edge, v = np.copy(gr['path']), np.copy(gr['dis']), np.copy(gr['edge']), np.copy(gr['v'])
            self.V.append(v)
            self.edge.append(edge)
            #print(dis)
            start = time()
            dis, path, size = self.floyd(dis, int(v), path)
            end = time() - start
            self.size.append(size)
            self.times.append(end)
            # print(V, times)
            print(self.size)
            print("Done")
    
    def save(self, name):
        self.findPath()
        df = pd.DataFrame({'n': self.V, 't': self.times, 'edge': self.edge, 'size': self.size})
        df.to_csv(name, header = True, index = None)

if __name__ == "__main__":
  # V, times = [],[]
  # v = 12
  # for i in range(40):
  #   print(v)
  #   V.append(v)
  #   path, dis = create(v)
  #   start = time()
  #   dis, path = floyd(dis, v, path)
  #   end = time() - start
  #   times.append(end)
  #   v*=1.09
  #   v = int(v)
  # print(V, times)
  # path, dis = create(5)
  # print('Path:\n{}\nDistance:\n{}'.format(path, dis))
  floyd  = Floyd(graph_floyd)
  floyd.save('/content/data/floyd_ThucNghiem.csv')