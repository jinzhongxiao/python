#!/usr/bin/env pythons
# -*- coding: utf-8 -*-
import numpy
import math
from tf import transformations

def isObject(item):
    #x, y, z, ox, oy, oz, ow
    if len(item) == 7:
        return True
    return False

def identity_matrix():
    #matrix 4*4
    return transformations.identity_matrix()

def markerToObject(Marker_Mat, Transform):
    return numpy.dot(Marker_Mat,Transform)

def getTransformMarix(src_mat, tar_mat):
    return numpy.dot(numpy.linalg.inv(src_mat), tar_mat)

def poseToMat(pose):
    trans = (pose[0], pose[1], pose[2])
    quat = (pose[3], pose[4], pose[5], pose[6])
    M_g_position = transToMat(trans)
    M_g_oren = quatToMat(quat)
    pose44 = numpy.dot(M_g_position, M_g_oren)
    return pose44

def matToPose(matrix):
    pose = [0,0,0,0,0,0,0]
    (pose[0], pose[1], pose[2]) = matToTrans(matrix)
    (pose[3], pose[4], pose[5], pose[6]) = matToQuat(matrix)
    return pose

def matToTrans(matrix):
    return transformations.translation_from_matrix(matrix)

def transToMat(transform):
    #(x,y,z)
    return transformations.translation_matrix(transform)

def matToQuat(matrix):
    return transformations.quaternion_from_matrix(matrix)

def quatToMat(quaternion):
    #(ox,oy,oz,ow)
    return transformations.quaternion_matrix(quaternion)

def matToEular(matrix, axes='sxyz'):
    return transformations.euler_from_matrix(matrix, axes='sxyz')

def eularToMat(roll, pitch, yaw, axes='sxyz'):
    return transformations.euler_matrix(roll, pitch, yaw, axes)

def eularToQuat(roll, pitch, yaw, axes='sxyz'):
    return transformations.quaternion_from_euler(roll, pitch, yaw, axes)

def quatToEular(quaternion, axes='sxyz'):
    return transformations.euler_from_quaternion(quaternion, axes)
