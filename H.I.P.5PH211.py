from visual import *
rocket = cylinder(radius=1.85,height=68.4,color=color.cyan)#Our Rocket which is a cylinder
A = 816.6#Cross sectional area -> 2(pi)rh + 2pir^2
cd = 0.8#Drag coeff, which is given.
g = vector(0.0,-9.8,0.0)#gravity
v = vector(0.0,0.0,0.0)#velocity starts at zero
s = vector(0.0,0.0,0.0)#position starts at zero since we take off from the ground
sm = 505846#Starting mass of our rocket in kg
fm = 13150 #Mass after fuel burning in kg
D = vector(0.0,0.0,0.0)#Defined Drag as a vector
fT = vector(0.0,5885000,0.0)#Force vector of thrust in Newtons.
t = 0.0#Time
dt = 1.0#Change in time

while t<138.0:
    rate(10)
    ml = (sm-fm)/180#ml is Mass Loss. So i am taking the average mass loss per second here.
    p = (0.289*e**(1.73-.000157*mag(s)))#equation for the change in the density of the air.
    D = .5*A*cd*p*mag(v)**2*norm(g)#Drag which involves cross sectional area, drag coeff, density of air and the magnitude of velocity squared times the norm vector of g since you cant square a vector 
    Fnet = fT - (D + (sm-ml*dt)*g)#Fnet is our Thrust minus our Drag plus our Mass times Gravity. So o=the Fnet is constantly changing dur to the increase in Drag.
    a = Fnet/(sm-ml*dt)#Accel = Fnet / Changing mass. 
    v = v + a*dt
    s = s + v*dt
    rocket.pos = s
    t = t + dt
    print 't=',t,'s=',s,'v=',v#Printing v and t are essential so I know when my rocket is at 137 seconds and how fast it is going at that time.

