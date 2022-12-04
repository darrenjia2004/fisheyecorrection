import math
import numpy as np

#calculates the relative distance between an object at x,y on screen and camera
def calculateDistance(x,y,yaw,pitch,roll,altitude):
    #camera specs
    horizontalAFOV=math.radians(38.7)
    verticalAFOV=math.radians(50)

    #converts yaw pitch roll from degrees to radians
    yaw=math.radians(yaw)
    pitch=math.radians(pitch)
    roll=math.radians(roll)

    #creates a vector in the camera's coordinate system that points to landing pad
    v=np.matrix([[2*y*math.tan(verticalAFOV/2)],[2*x*math.tan(horizontalAFOV/2)],[1]])
    print(v)
    
    #converts vector into world coordinate system
    rotz=np.matrix([[math.cos(yaw), -math.sin(yaw), 0], [math.sin(yaw), math.cos(yaw),0], [0,0,1]])
    roty=np.matrix([[math.cos(pitch), 0, math.sin(pitch)], [0, 1, 0], [-math.sin(pitch),0,math.cos(pitch)]])
    rotx=np.matrix([[1, 0, 0], [0, math.cos(roll),-math.sin(roll)], [0,math.sin(roll),math.cos(roll)]])
    v=np.matmul(rotz,v)
    v=np.matmul(rotx, v)
    v=np.matmul(roty, v)

    #calculate intersection of vector and ground
    t=altitude/(v[2,0])
    xdirection = (t*v[0,0])
    ydirection = (t*v[1,0])

    vw = np.matrix([[xdirection],[ydirection],[altitude]])

    #rotz= np.matrix([[math.cos(yaw), -math.sin(yaw)], [math.sin(yaw),math.cos(yaw)]])
    #vw=np.matmul(rotz, vw)
    print (vw)

calculateDistance(-0.29166666666,0.29765625,0,0,0,159)