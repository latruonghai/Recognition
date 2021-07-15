import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

namefile1 = 'data_new/floyd_time_ThucNghiem.csv'
namefile2 = 'data_new/bellman_time_ThucNghiem.csv'
namefile3 = 'data_new/dijsktra_time_ThucNghiem.csv'

def coef(X):
    regr=LinearRegression().fit(X, Y)
    a = round(regr.coef_[0],19) if regr.coef_[0]!=0.0 else 1.0
    plt.plot(X, Y, '.', X, a*X, '.')
    return a

def readDataSet(fp, type='t'):
    data=pd.read_csv('/content/data/floyd_ThucNghiem.csv')[0:50]
##print(data)
    X0=data['n'].values.reshape(-1,1)
    Y=data['t'].values
    edge = data['edge'].values.reshape(-1, 1)
    plt.scatter(X0, Y)
    return X0, Y, edge, data
def modify(fn, columns_name, data, *arg):
    edge, V = arg
    X = fn(V)
    a=coef(X)
    data['{}*{}'.format(a, columns_name)]=a*X
    data[columns_name]=(data['{}*e*v^2'.format(a)]-Y)**2
    return data
# def modify(fn):
    
#     def wrapper(columns_name, data, *arg):
#         edge, V = arg
#         X = fn(V, edge)
#         a = coef(X)
#         data['{}*{}'.format(a, columns_name)]=a*X
#         data[columns_name]=(data['{}*e*v^2'.format(a)]-Y)**2
#         return data
#     return wrapper
# @modify
def sqrt(V, e):
    return np.sqrt(V)

# @modify
def n(V, e):
    return n

# @modify
def n2(V, e):
    return V**2

# @modify
def n3(V, e):
    return V**3
    # """
# **e*v^2**"""
# @modify
def elogv(V, e):
    return V*(e*np.log2(V))

def ev2(V, e):
    return e*V**2
# X=X0**2 * edge
def log(V,e):
    return np.log(V)
def calculate(V, edge, data, listOfName):
    for name in listOfName:
        
        data = modify(fn=eval(name), name, data, edge, V)
    return data



def getPlot(data):
    MSE_sqrt=np.average(data['sqrt(n) squared_error'])
    MSE_log=np.average(data['log(n) squared_error'])
    MSE_n=np.average(data['n squared_error'])
    MSE_nlog=np.average(data['elog(v) squared_error'])
    MSE_n3=np.average(data['n^3 squared_error'])
    MSE_mn2=np.average(data['ev2 squared_error'])
    MSE_n2=np.average(data['n^2 squared_error'])
    # MSE_n2=np.average(data['n^2 squared_error'])
    data = data.append({'n':'MSE','sqrt(n) squared_error':MSE_sqrt,'log(n) squared_error':MSE_log,'n squared_error':MSE_n,'vlog(e) squared_error':MSE_nlog,'n3 squared_error':MSE_n3, 'n^2 squared_error':MSE_n2,'ev2 squared_error':MSE_mn2},ignore_index=True)
    return data

if __name__ == "__main__":
    listOfName = ['n', 'sqrt', 'n3', 'n2', 'elogv', 'ev2','log']
    V, Y, edge, data_floyd = readDataSet('floyd_size_ThucNghiem.csv')
    V, Y, edge, data_dijsktra = readDataSet('dijsktra_size_ThucNghiem.csv')
    V, Y, edge, data_bellman = readDataSet('bellman_size_ThucNghiem.csv')
    data_floyd = calculate(V, edge, data_floyd, listOfName)
    data_bellman = calculate(V, edge, data_bellman, listOfName)
    data_dijsktra = calculate(V, edge, data_dijsktra, listOfName)
    data_bellman =  getPlot(data_bellman)
    data_floyd = getPlot(data_floyd)
    data_dijsktra = getPlot(data_dijsktra)
    # data = data.append({'n':'MSE','sqrt(n) squared_error':MSE_sqrt,'log(n) squared_error':MSE_log,'n squared_error':MSE_n,'vlog(e) squared_error':MSE_nlog,'n^3 squared_error':MSE_n3, 'n^2 squared_error':MSE_n2,'e*v^2 squared_error':MSE_mn2},ignore_index=True)
    
