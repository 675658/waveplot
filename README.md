# waveplot
这个类是matplotlib.pyplot的一个封装,用于在多线程下绘制动态图形
示例:
```python
from waveplot import *
import time
import threading
import math
import matplotlib
matplotlib.use('TKAgg')
waveplt=waveplot(line=2,row=1,x_scroll_size=100,label=['1','2'],title=['1','2'],y_limit=[[-1,1],[-1,1]]) # 创建绘图,2行1列,横向最大显示100个点,子图1,2的标签分别为'1','2',标题分别为'1','2',y轴范围分别为[-1,1],[-1,1]
t=0
def a():    # 模拟mqtt接收函数
    global t
    global waveplt
    while True:
        waveplt.plot(x=[t],y=[math.sin(t)],subgraph=1)  # 绘图 x=[t] y=[sin(t)] 子图1
        waveplt.plot(x=[t],y=[math.cos(t)],subgraph=2)  # 绘图 x=[t] y=[cos(t)] 子图2
        t=t+0.1
        time.sleep(0.1)

if __name__ == '__main__':
    waveplt.subplts[0].set_ylim(-1,1)
    t1=threading.Thread(target=a)       # 创建进程
    t1.start()                          # 开始进程
    waveplt.show()                      # 接收绘图请求



```
