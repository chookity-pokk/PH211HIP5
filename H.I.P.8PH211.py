from visual import *
s = vector(0.0,90.5,0.0)
v = vector(0.0,0.0,0.0)
g = vector(0.0,-9.8,0.0)

k = 47.98
x = 61

A = pi*.5**2
cD = .82
p = 1.225
m = 70
human = cylinder(radius=.5,color=color.cyan,pos = s)

t = 0.0
dt = 0.5

Fg = -g
D = vector(0.0,0.0,0.0)
Fs = vector(0.0,0.0,0.0)
while s.y>61.0:
    rate(10)
    D = .5*cD*p*A*mag(v)**2*norm(g)
    Fg = -g
    Fnet = D + Fg
    a = Fnet/m
    v = v + a * dt
    s = s + v * dt
    human.pos = s
    t = t + dt
    
while s.y<61.0:
    rate(10)
    Fs = k * (s.y-30)
    Fnet = Fg + Fs + D
    a = Fnet/m
    v = v + a * dt
    s = s + v * dt
    t = t + dt
    print 'D=',D
#D asymtotically approaches -9.8
