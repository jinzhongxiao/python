#!/usr/bin/env python
import numpy
import utils as util



trans = (1.1306105592788473, -0.023380240667990177, 0.14249669943110535)
quat = (-7.527518111164107e-06, 5.9763349822339885e-06, 3, 0.6004010900676073)
M_g_position = util.transToMat(trans)
M_g_oren = util.quatToMat(quat)

pose = numpy.dot(M_g_position, M_g_oren)



trans1 = (4.317941566083451, 1.5709863840103493, 0.05491839929534929)
quat1 = (-0.32174980469150205, 0.6295233496884052, -0.629746763082377, -0.32186399265114907)
M_g_position1 = util.transToMat(trans1)
M_g_oren1 = util.quatToMat(quat1)

pose1 = numpy.dot(M_g_position1, M_g_oren1)

poseM = numpy.asmatrix(pose)
pose1M = numpy.asmatrix(pose1)
gazebo_pose44 = numpy.dot(poseM.I, pose1M )
gz_pose = util.matToPose(gazebo_pose44)


print gz_pose
