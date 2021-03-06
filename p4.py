from math import *
from kandinsky import *
from ion import *
from time import *

false = 0
true = 1

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
        s.g[i].append(0)
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
  p = 2
  sco = 0
  lsco = 0
  sca = 0
  w = 0

  def __init__(s, g):
    s.g = g
    s.cr = s.g.x * s.g.y
    return

  def dgm(s):
    x = s.g.gox
    y = s.g.goy
    for i in s.g.g:
        for j in i:
          #print(x," ",y)
          if(j==1):
            fill_rect(x+2, y+2, s.g.cw-2, s.g.ch-2, s.g.c1)
            #fill_circle(s.g.jx(x),s.g.jy(y),int(s.g.ch/2),s.g.c1)
          elif(j==2):
            #fill_circle(s.g.jx(x),s.g.jy(y),int(s.g.ch/2),s.g.c2)
            fill_rect(x+2, y+2, s.g.cw-2, s.g.ch-2, s.g.c2)
          elif(j == 3):
            #draw_circle(s.g.jx(x),s.g.jy(y),int(s.g.ch/2),s.g.c1)
            fill_rect(x+2, y+2, s.g.cw-2, s.g.ch-2, s.g.c1)
            fill_rect(x+4, y+4, s.g.cw-8, s.g.ch-8, (255,255,255))
          elif(j == 4):
            #draw_circle(s.g.jx(x),s.g.jy(y),int(s.g.ch/2),s.g.c2)
            fill_rect(x+2, y+2, s.g.cw-2, s.g.ch-2, s.g.c2)
            fill_rect(x+4, y+4, s.g.cw-8, s.g.ch-8, (255,255,255))
          elif(j == 0):
            fill_rect(x+1, y+1, s.g.cw-1, s.g.ch-1, (255,255,255))

          x = x + s.g.cw
        x=s.g.gox
        y = y + s.g.ch
    s.dgmi()
    return

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
      fill_rect(x, y, s.g.cw, s.g.ch, (255,255,255))
      if(i == s.sco):
        #fill_circle(s.g.jx(x), s.g.jy(y), int(s.g.ch/2), c)
        fill_rect(x+2, y+2, s.g.cw-2, s.g.ch-2, c)
      else:
        #draw_circle(s.g.jx(x), s.g.jy(y), int(s.g.ch/2), c)
        fill_rect(x+2, y+2, s.g.cw-2, s.g.ch-2, c)
        fill_rect(x+4, y+4, s.g.cw-8, s.g.ch-8, (255,255,255))

    
    #draw_string(str(s.cr), 0, s.g.ch)
    return

  def onr(s):
    s.lsco = s.sco
    s.mv("right")
    s.ons(false)
    s.dgm()
    return

  def onl(s):
    s.lsco = s.sco
    s.mv("left")
    s.ons(false)
    s.dgm()
    return

  def mv(s, d):
    if(d == "right"):
      for i in range(s.g.x):
        s.sco = s.sco + 1
        if(s.sco >= s.g.x):
          s.sco = 0
        if(s.g.g[0][s.sco] != 1 and s.g.g[0][s.sco] != 2):
          return
    elif(d == "left"):
      for i in range(s.g.x):
        s.sco = s.sco - 1
        if(s.sco < 0):
          s.sco = s.g.x -1
        if(s.g.g[0][s.sco] != 1 and s.g.g[0][s.sco] != 2):
          return



  def ons(s, se):
    if(s.g.g[s.sca][s.lsco] != 1 and s.g.g[s.sca][s.lsco] != 2):
      s.g.g[s.sca][s.lsco] = 0

    for i in range(s.g.y):
      if(s.g.g[i][s.sco] == 1 or s.g.g[i][s.sco] == 2):
        if(i == 0):
          s.sca = 0
        else:
          s.sca = i-1
        break
      if(i == s.g.y -1):
        s.sca = i
        break

    if(se == false):
      s.g.g[s.sca][s.sco] = s.p + 2
    if(se == true):
      s.g.g[s.sca][s.sco] = s.p
      s.cr = s.cr - 1
      if(s.cr <= 0):
        return
      if(s.sca != 0):
        s.sca = s.sca -1
      else:
        if(s.lsco - s.sco < 0):
          s.onr()
        else:
          s.onl()
    return

  def onp(s):
    s.ons(true)
    if(s.cr == 0):
      s.p = 0
      s.dgm()
      return
    elif(s.p == 2):
      s.p = 1
    else:
      s.p = 2
    s.ons(false)
    s.dgm()
    return

  def tick(s):
    if(g.p <= 0):
      fill_rect(0, 0, s.g.gox, 330, (255,255,255))
      draw_string("partie terminee.", 0, 0)
      g.w = 1


g=game(grid(7,6))
g.g.dgd()
g.ons(false)
g.dgm()

t = monotonic()
gt = monotonic()

while(g.w == 0):
  if((t + 0.25) < monotonic()):
    if(keydown(KEY_RIGHT)):
      t = monotonic()
      g.onr()
    if(keydown(KEY_LEFT)):
      t = monotonic()
      g.onl()
    if(keydown(KEY_DOWN) or keydown(KEY_OK) or keydown(KEY_EXE)):
      t = monotonic()
      g.onp()
  if((gt + 0.1) < monotonic()):
    g.tick()
    gt = monotonic()
    
    #print(g.sc)
