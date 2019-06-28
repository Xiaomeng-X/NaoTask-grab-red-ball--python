#-*-encoding:UTF-8-*-
import almath
import time
import re
from naoqi import ALProxy
from naoqi import ALModule
from VisualTask import BallDetect

class TargetSearchModule(ALModule):
    def __init__(self,name,robot_ip,robot_port,object_name):
        ALModule.__init__(self,name)
        self.robot_ip = robot_ip
        self.robot_port = robot_port
        self.motionProxy = ALProxy("ALMotion",robot_ip,robot_port)
        self.postureProxy = ALProxy("ALRobotPosture",robot_ip,robot_port)
        self.motionProxy.wakeUp()
        self.postureProxy.goToPosture("StandInit",0.3)
        self.searchOut = False
        self.rotate = 120*almath.TO_RAD
        self.rotateTime = 1
        self.useSensors = False
        self.matrix=[(0,0) for i in range(10)]
        pattern_ball = re.compile(r"ball")
        match_ball = pattern_ball.search(object_name)
        if match_ball:
            self.search_obj = BallDetect(object_name,robot_ip,robot_port)


    def doSearch(self):
        print "TargetSearchModule doSearch()"
        self.motionProxy.setStiffnesses("Head",1.0)
        self.doHeadSearch()
        #若没有搜索到目标，从当前位置移动一定距离再次进行搜索
        while self.searchOut==False and self.rotateTime <3:
        	self.motionProxy.moveTo(1.0,0.0,0.0)
        	self.doHeadSearch()
        	if self.searchOut==True:
        		break
        	self.motionProxy.moveTo(0.0,0.0,self.rotate)
        	self.rotateTime = self.rotateTime + 1

        if self.searchOut==False:
            print  "haven't find"
            return False

        else :
            print "find"
            #若搜索到目标，调整机器人身体角度，并把头的位置调正
            angles = self.motionProxy.getAngles("HeadYaw",self.useSensors)
            self.motionProxy.setAngles("HeadYaw",0,0.2)
            time.sleep(3)
            #self.motionProxy.setStiffnesses("Head",0.0)
            self.motionProxy.moveTo(0.0,0.0,angles[0])
            self.searchOut = False
            return True

    def doHeadSearch(self):
        print "TargetSearchModule doHeadSearch()"
        #正前方搜索
        fault_tolerance_times = 2
        while fault_tolerance_times>0:
            print 1
            for i in range(10):
                self.search_obj.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
                self.search_obj.showBallPosition()
                self.matrix[i] = self.search_obj.getBallData()
            self.matrix = sorted(self.matrix)
            #debug 
            string = ""
            for i in range(10):
                string += str(self.matrix[i])
            print string
            midE = self.matrix[(len(self.matrix)-1)/2+3]
            if midE!=(0,0):
                count = 0
                for i in range(10):
                    if self.matrix[i][0]>midE[0]-10 and self.matrix[i][0]<midE[0]+10 and self.matrix[i][1]>midE[1]-10 and self.matrix[i][1]<midE[1]+10:
                        count += 1
                if count>2:
                    self.searchOut=True
                    break
            fault_tolerance_times = fault_tolerance_times-1

        #左转30度搜索，一共2次
        times = 0
        while self.searchOut==False and times<2:
            print "左转45度搜索"
            self.motionProxy.changeAngles("HeadYaw",45*almath.TO_RAD,0.2)
            fault_tolerance_times = 2
            while fault_tolerance_times>0:
                for i in range(10):
                    self.search_obj.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
                    self.search_obj.showBallPosition()
                    self.matrix[i] = self.search_obj.getBallData()
                self.matrix = sorted(self.matrix)
                #debug
                string = ""
                for i in range(10):
                    string += str(self.matrix[i])
                print string
                print 2
                midE = self.matrix[(len(self.matrix)-1)/2+3]
                if midE!=(0,0):
                    count = 0
                    for i in range(10):
                        if self.matrix[i][0]>midE[0]-10 and self.matrix[i][0]<midE[0]+10 and self.matrix[i][1]>midE[1]-10 and self.matrix[i][1]<midE[1]+10:
                            count += 1
                    if count>2:
                        self.searchOut=True
                        break
                fault_tolerance_times = fault_tolerance_times-1
            times = times + 1

        #右转30度搜索，一共2次
        if self.searchOut==False:
            times = 0
            self.motionProxy.setAngles("HeadYaw",0,0.4)
            time.sleep(3)
            print "set yes"
        while self.searchOut==False and times<2:
            print "右转45度搜索"
            self.motionProxy.changeAngles("HeadYaw",-45*almath.TO_RAD,0.2)
            fault_tolerance_times = 2
            while fault_tolerance_times>0:
                for i in range(10):
                    self.search_obj.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
                    self.search_obj.showBallPosition()
                    self.matrix[i] = self.search_obj.getBallData()
                self.matrix = sorted(self.matrix)
                #debug
                string = ""
                for i in range(10):
                    string += str(self.matrix[i])
                print string
                print 3
                midE = self.matrix[(len(self.matrix)-1)/2+3]
                if midE!=(0,0):
                    count = 0
                    for i in range(10):
                        if self.matrix[i][0]>midE[0]-10 and self.matrix[i][0]<midE[0]+10 and self.matrix[i][1]>midE[1]-10 and self.matrix[i][1]<midE[1]+10:
                            count += 1
                    if count>2:
                        self.searchOut=True
                        break
                fault_tolerance_times = fault_tolerance_times-1
            times = times + 1
        if self.searchOut==False:
            self.motionProxy.setAngles("HeadYaw",0,0.2)
            time.sleep(5)
        #self.motionProxy.setStiffnesses("Head",0.0)



    




