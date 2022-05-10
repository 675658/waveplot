from cProfile import label
from time import sleep
from numpy import double, where
import threading
import matplotlib.pyplot as plt

class waveplot:
    def __init__(self,line:int,row:int,x_scroll_size:int,label:list[str],title:list[str],y_limit:list[list[int or double,int or double]]):
        self.x=[]
        self.y=[]
        self.gfig=plt.figure()
        self.subgraph_num=line*row
        if self.subgraph_num<=1:
            self.subplts=[self.gfig.subplots(line,row)]
        else:
            self.subplts=self.gfig.subplots(line,row)
        self.__x_scrool_size=x_scroll_size
        self.__semaphore = threading.Semaphore(0)
        self.__label=label
        self.y_limit=y_limit
        self.title=title
        for i in range(self.subgraph_num):
            self.x.append([])
            self.y.append([])

    def flush(self):
        self.__semaphore.release()
        
    def show(self):
        while True:
            self.__semaphore.acquire()
            for p_subplt in range(len(self.subplts)):
                self.subplts[p_subplt].cla()
                self.subplts[p_subplt].set_title(self.title[p_subplt])
                self.subplts[p_subplt].set_ylim(self.y_limit[p_subplt][0],self.y_limit[p_subplt][1])
                self.subplts[p_subplt].plot(self.x[p_subplt],self.y[p_subplt],label=self.__label[p_subplt])
            plt.pause(0.001)

    def plot(self,x:list[int or float],y:list[int or float],subgraph:int):
        if subgraph > self.subgraph_num:
            pass
        if len(self.x[subgraph-1]) <= self.__x_scrool_size:
            self.x[subgraph-1]=self.x[subgraph-1][0:len(self.x[subgraph-1])]+x
            self.y[subgraph-1]=self.y[subgraph-1][0:len(self.y[subgraph-1])]+y
        else:
            self.x[subgraph-1]=self.x[subgraph-1][len(x):len(self.x[subgraph-1])]+x
            self.y[subgraph-1]=self.y[subgraph-1][len(y):len(self.y[subgraph-1])]+y