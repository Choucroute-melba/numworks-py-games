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
    s.cw=int(s.gw/x-1)
    s.ch=int(s.gh/y-1)
    s.gox = s.sw-s.gw
    s.goy = s.sh-s.gh

    for i in range(y):
      for j in range(x):
        s.g[i].append(0)
      s.g.append([])
      #print(str(s.g))
    print(x," ",y," ",s.cw," ",s.ch)
    draw_string("x " + str(x) + " : y " + str(y) + " : cw " + str(s.cw) + " : ch " + str(s.ch), 0, 0)
    
  def dg(s):
    draw_line(s.gox, s.goy, s.sw, s.goy, s.c) # horizontal
    draw_line(s.gox, s.goy, s.gox, s.sh, s.c) # vertical
    for i in range(s.y):
        draw_line(s.gox, s.goy + i * s.ch, s.sw, s.goy + i * s.ch, s.c)
    for i in range(s.x):
        draw_line(s.gox + i * s.cw, s.goy, s.gox + i * s.cw, s.goy, s.c)

    return
    
g=grid(10,8)
g.dg()
