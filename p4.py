﻿from math import *
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

<<<<<<< HEAD

g=game(grid(7,6))
g.g.dgd()
=======
      x = s.gox
      y = s.goy
      for i in s.g:
=======
    x = s.g.gox
    y = s.g.goy
    for i in s.g.g:
>>>>>>> 930a4e0 (create game class)
        for j in i:
          #print(x," ",y)
          if(j==1):
            fill_circle(s.g.jx(x),s.g.jy(y),int(s.g.ch/2),s.g.c1)
          elif(j==2):
            fill_circle(s.g.jx(x),s.g.jy(y),int(s.g.ch/2),s.g.c2)
          x = x + s.g.cw
        x=s.g.gox
        y = y + s.g.ch
=======
  def dgmi(s):
    x = 0
    y = 0
    if(s.p == 1):
      c = s.g.c1
    elif(s.p == 2):
      c = s.g.c2
    else:
      c = (0,255,0)

    for i in range(s.g.x):
      x = i * s.g.cw
      if(i == s.sc):
        #fill_circle(s.g.jx(x), s.g.jy(y), int(s.g.ch/2), c)
        fill_rect(x+2, y+2, s.g.cw-2, s.g.ch-2, c)
      else:
        #draw_circle(s.g.jx(x), s.g.jy(y), int(s.g.ch/2), c)
        fill_rect(x+2, y+2, s.g.cw-2, s.g.ch-2, c)
        fill_rect(x+4, y+4, s.g.cw-8, s.g.ch-8, (255,255,255))
>>>>>>> gist
    return


<<<<<<< HEAD
class game:
  def __init__(s, goy):
    return    
    
g=grid(7,6)
g.dgd()
>>>>>>> 2d53fce (next)
=======
g=game(grid(7,6))
g.g.dgd()
>>>>>>> 930a4e0 (create game class)
g.dgm()
