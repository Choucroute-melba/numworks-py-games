from math import *
from kandinsky import *


class grid:
  c=[0,0,0]

  x=0
  y=0
  sw=320
  sh=220
  gw=320
  gh=170
  cw=0
  ch=0
  g=[[]]
  
  def __init__(s,x,y):
    s.x=x
    s.y=y
    s.cw=s.gw/x-1
    s.ch=s.gh/y-1  
    for i in range(y):
      for j in range(x):
        s.g[i].append(0)
      s.g.append([])
      #print(str(s.g))
    print(x," ",y," ",s.cw," ",s.ch)
    
  def dg(s):
    draw_line(s.sw-s.gw, s.sh-s.gh, s.sw, s.sh-s.gh, s.c)
    draw_line(s.sw-s.gw, s.sh-s.gh, s.sw-s.gw, s.sh, s.c)
    return
    
g=grid(10,8)
g.dg()
