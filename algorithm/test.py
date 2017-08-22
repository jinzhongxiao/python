#!/usr/bin/env python
import math
def findNearestObj( objNames, objPoses):

    if len(objNames) <= 1:
        return objNames, objPoses, math.sqrt((objPoses[0][0]*objPoses[0][0])+(objPoses[0][1]*objPoses[0][1])+(objPoses[0][2]*objPoses[0][2]))
    
    dis = math.sqrt((objPoses[0][0]*objPoses[0][0])+(objPoses[0][1]*objPoses[0][1])+(objPoses[0][2]*objPoses[0][2]))
    return [objNames[0],objPoses[0],dis ]\
        if findNearestObj( objNames[1:], objPoses[1:])[2] > dis else findNearestObj( objNames[1:], objPoses[1:])



objs = ['a']
objpos = [[2,2,2]]

print findNearestObj(objs, objpos)