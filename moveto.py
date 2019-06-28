#-*-coding:utf-8 -*-

import sys
import config
from naoqi import ALProxy

def move(robot_ip,robot_port,x,y,angle):
  ## flag=0 left flag=1 right
  motionProxy = config.loadProxy("ALMotion",robot_ip,robot_port)

  #Set NAO in stiffness On
  # config.StiffnessOn(motionProxy)
  # config.PoseInit(motionProxy)

  #####################
  ## Enable arms control by Walk algorithm
  #####################
  motionProxy.setWalkArmsEnabled(True, True)
  #~ motionProxy.setWalkArmsEnabled(False, False)

  #####################
  ## FOOT CONTACT PROTECTION
  #####################
  #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
  motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
  X = x*0.02
  Y = y*0.02
  Theta = angle
  motionProxy.post.walkTo(X, Y, Theta)
  # wait is useful because with post walkTo is not blocking function
  motionProxy.waitUntilWalkIsFinished()
