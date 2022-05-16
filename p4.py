from math import *
from kandinsky import *


class grid:
  c=[0,0,0]
  c1=[255,0,0]
  c2=[0,0,255]

  x=0
  y=0
  sw=330
  sh=230
  gw=330
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
        s.g[i].append(2)
      s.g.append([])
      #print(str(s.g))
    print(x," ",y," ",s.cw," ",s.ch)
    #draw_string("x " + str(s.x) + " | y " + str(s.y) + " | cw " + str(s.cw) + " | ch " + str(s.ch), 0, 0)

  def dgd(s):
    #draw_line(s.gox, s.goy, s.sw, s.goy, s.c) # horizontal
    #draw_line(s.gox, s.goy, s.gox, s.sh, s.c) # vertical

    # draw lines
    for i in range(s.y):
        draw_line(s.gox, s.goy + i * s.ch, s.sw, s.goy + i * s.ch, s.c)
    draw_line(s.gox, s.goy + s.y * s.ch, s.sw, s.goy + s.y * s.ch, s.c)

    # draw columns
    for i in range(s.x):
        draw_line(s.gox + i * s.cw, s.goy, s.gox + i * s.cw, s.sh, s.c)
    draw_line(s.gox + s.x * s.cw, s.goy, s.gox + s.x * s.cw, s.sh, s.c)

    return

  def jx(s,x):
    return int(x+(s.cw/2))

  def jy(s, y):
    return int(y+(s.ch/2))



class game:
  def __init__(s, g):
    s.g = g
    return

  def dgm(s):
<<<<<<< HEAD
    x = s.g.gox
    y = s.g.goy
    for i in s.g.g:
        for j in i:
          #print(x," ",y)
          if(j==1):
            fill_circle(s.g.jx(x),s.g.jy(y),int(s.g.ch/2),s.g.c1)
          elif(j==2):
            fill_circle(s.g.jx(x),s.g.jy(y),int(s.g.ch/2),s.g.c2)
          x = x + s.g.cw
        x=s.g.gox
        y = y + s.g.ch
    return


g=game(grid(7,6))
g.g.dgd()
=======
      x = s.gox
      y = s.goy
      for i in s.g:
        for j in i:
          #print(x," ",y)
          if(j==1):
            fill_circle(s.jx(x),s.jy(y),int(s.ch/2),s.c1)
          elif(j==2):
            fill_circle(s.jx(x),s.jy(y),int(s.ch/2),s.c2)
          x = x + s.cw
        x=s.gox
        y = y + s.ch

  def jx(s,x):
    return int(x+(s.cw/2))
    
  def jy(s, y):
    return int(y+(s.ch/2))

class game:
  def __init__(s, goy):
    return    
    
g=grid(7,6)
g.dgd()
>>>>>>> 2d53fce (next)
g.dgm()
