#-*-coding:utf-8 -*-

import motion
import config

def posinit(robot_ip,robot_port):
    #该方法为正常初始姿势程序
    proxy = config.loadProxy("ALMotion",robot_ip,robot_port)

    # Define The Initial Position
    HeadYawAngle=0.0
    HeadPitchAngle=0.0

    ShoulderPitchAngle = +80.0
    ShoulderRollAngle  = +20.0
    ElbowYawAngle      = -80.0
    ElbowRollAngle     = +0.0
    WristYawAngle      = + 0.0
    HandAngle          = + 0.0

    HipYawPitchAngle   = + 0.0
    HipRollAngle       = + 0.0
    HipPitchAngle      = -25.0
    KneePitchAngle     = +40.0
    AnklePitchAngle    = -20.0
    AnkleRollAngle     = + 0.0

    # Get the Robot Configuration
    robotConfig = proxy.getRobotConfig()
    robotName = ""
    for i in range(len(robotConfig[0])):
        if (robotConfig[0][i] == "Model Type"):
            robotName = robotConfig[1][i]

    if (robotName == "naoH25") or\
       (robotName == "naoAcademics"):

        Head     = [HeadYawAngle, HeadPitchAngle]

        LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle, WristYawAngle, HandAngle]
        RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle, WristYawAngle, HandAngle]

        LeftLeg  = [HipYawPitchAngle, +HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
        RightLeg = [HipYawPitchAngle, -HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, -AnkleRollAngle]

    elif (robotName == "naoH21") or\
         (robotName == "naoRobocup"):

        Head     = [HeadYawAngle, HeadPitchAngle]

        LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle]
        RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle]

        LeftLeg  = [HipYawPitchAngle, +HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
        RightLeg = [HipYawPitchAngle, -HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, -AnkleRollAngle]

    elif (robotName == "naoT14"):

        Head     = [HeadYawAngle, HeadPitchAngle]

        LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle, WristYawAngle, HandAngle]
        RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle, WristYawAngle, HandAngle]

        LeftLeg  = []
        RightLeg = []

    elif (robotName == "naoT2"):

        Head     = [HeadYawAngle, HeadPitchAngle]

        LeftArm  = []
        RightArm = []

        LeftLeg  = []
        RightLeg = []

    else:
        print "ERROR : Your robot is unknown"
        print "This test is not available for your Robot"
        print "---------------------"
        exit(1)

    # Gather the joints together
    pTargetAngles =  Head+LeftArm + LeftLeg + RightLeg + RightArm

    # Convert to radians
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]

    #------------------------------ send the commands -----------------------------
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    # We set the fraction of max speed
    pMaxSpeedFraction = 0.2
    # Ask motion to do this with a blocking call
    proxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)

def posinit2(HeadYawAngle, HeadPitchAngle,robot_ip,robot_port):
    #该方法中可以设置头部俯仰角度
    proxy = config.loadProxy("ALMotion",robot_ip,robot_port)

    # Define The Initial Position

    ShoulderPitchAngle = +80.0
    ShoulderRollAngle  = +20.0
    ElbowYawAngle      = -80.0
    ElbowRollAngle     = +0.0
    WristYawAngle      = + 0.0
    HandAngle          = + 0.0

    HipYawPitchAngle   = + 0.0
    HipRollAngle       = + 0.0
    HipPitchAngle      = -25.0
    KneePitchAngle     = +40.0
    AnklePitchAngle    = -20.0
    AnkleRollAngle     = + 0.0

    # Get the Robot Configuration
    robotConfig = proxy.getRobotConfig()
    robotName = ""
    for i in range(len(robotConfig[0])):
        if (robotConfig[0][i] == "Model Type"):
            robotName = robotConfig[1][i]

    if (robotName == "naoH25") or\
       (robotName == "naoAcademics"):

        Head     = [HeadYawAngle, HeadPitchAngle]

        LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle, WristYawAngle, HandAngle]
        RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle, WristYawAngle, HandAngle]

        LeftLeg  = [HipYawPitchAngle, +HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
        RightLeg = [HipYawPitchAngle, -HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, -AnkleRollAngle]

    elif (robotName == "naoH21") or\
         (robotName == "naoRobocup"):

        Head     = [HeadYawAngle, HeadPitchAngle]

        LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle]
        RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle]

        LeftLeg  = [HipYawPitchAngle, +HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
        RightLeg = [HipYawPitchAngle, -HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, -AnkleRollAngle]

    elif (robotName == "naoT14"):

        Head     = [HeadYawAngle, HeadPitchAngle]

        LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle, WristYawAngle, HandAngle]
        RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle, WristYawAngle, HandAngle]

        LeftLeg  = []
        RightLeg = []

    elif (robotName == "naoT2"):

        Head     = [HeadYawAngle, HeadPitchAngle]

        LeftArm  = []
        RightArm = []

        LeftLeg  = []
        RightLeg = []

    else:
        print "ERROR : Your robot is unknown"
        print "This test is not available for your Robot"
        print "---------------------"
        exit(1)

    # Gather the joints together
    pTargetAngles =  Head+LeftArm + LeftLeg + RightLeg + RightArm

    # Convert to radians
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]

    #------------------------------ send the commands -----------------------------
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    # We set the fraction of max speed
    pMaxSpeedFraction = 0.2
    # Ask motion to do this with a blocking call
    proxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)

