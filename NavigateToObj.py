import config
import posinit
import moveto
from VisualTask import BallDetect
import almath
import vision_definitions as vd
from naoqi import ALProxy
from naoqi import ALModule
high=480   
wide=640
class NavigateToObj(ALModule):
    def __init__(self,name,robot_ip,robot_port):
        ALModule.__init__(self,name)
        self.robot_ip = robot_ip
        self.robot_port = robot_port
        self.matrix=[(0,0) for i in range(5)]
        self.motionProxy = ALProxy("ALMotion",robot_ip,robot_port)

    def NavigateToBall(self,message):
        print "NavigateToObj NavigateToBall()"
        self.message = message
        #posinit.posinit(self.robot_ip,self.robot_port);
        tts = ALProxy("ALTextToSpeech",self.robot_ip,self.robot_port)
        tts.say("i will move towards this direction!")
        posinit.posinit(self.robot_ip,self.robot_port)
        ballDetect = BallDetect(self.message, self.robot_ip, resolution=vd.kVGA, writeFrame=True)
        ballDetect.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
        center = ballDetect.getBallData()
        print center
        while center[1]<450:
            if center!=(0,0):
                tts.say("I will go ahead")
                if center[1]<400:
                    step=8
                else:
                    step=1
                moveto.move(self.robot_ip,self.robot_port,step,0,0)
                while (center[1]<450 and (center[0] > (wide/2+50)) or (center[0] < (wide/2-50))):
                    if center!=(0,0):
                        tts.say("I am checking the coordinate x bigger")
                        print "I am checking the coordinate x bigger"
                        #if center[0] > (wide/2+50):
                        #    moveto.move(self.robot_ip,self.robot_port,0,-5,0)
                        #elif center[0] < (wide/2-50):
                        #    moveto.move(self.robot_ip,self.robot_port,0,5,0)
                        if center[0] > (wide/2+50):
                            self.motionProxy.changeAngles("HeadYaw",-3*almath.TO_RAD,0.8)
                        elif center[0] < (wide/2-50):
                            self.motionProxy.changeAngles("HeadYaw",3*almath.TO_RAD,0.8)
                    fault_tolerance_times = 2
                    while fault_tolerance_times>0:
                        for i in range(5):
                            ballDetect.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
                            self.matrix[i] = ballDetect.getBallData()
                        self.matrix = sorted(self.matrix,key=lambda x: (x[1], x[0]))
                        #debug 
                        string = ""
                        for i in range(5):
                            string += str(self.matrix[i])
                        print string
                        print fault_tolerance_times
                        midE = self.matrix[len(self.matrix)-2]
                        if midE!=(0,0):
                            count = 0
                            for i in range(5):
                                if self.matrix[i][0]>midE[0]-10 and self.matrix[i][0]<midE[0]+10 and self.matrix[i][1]>midE[1]-10 and self.matrix[i][1]<midE[1]+10:
                                    count += 1
                            if count>2:
                                center = midE
                                break
                        fault_tolerance_times = fault_tolerance_times-1
                    print center
                angles = self.motionProxy.getAngles("HeadYaw",False)
                self.motionProxy.setAngles("HeadYaw",0,0.5)
                self.motionProxy.moveTo(0.0,0.0,angles[0])
                print "I have checked coordinate X firstly"
            midE = (0,0)
            fault_tolerance_times = 2
            while fault_tolerance_times>0:
                for i in range(5):
                    ballDetect.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
                    self.matrix[i] = ballDetect.getBallData()
                self.matrix = sorted(self.matrix,key=lambda x: (x[1], x[0]))
                #debug 
                string = ""
                for i in range(5):
                    string += str(self.matrix[i])
                print string
                print fault_tolerance_times
                midE = self.matrix[len(self.matrix)-2]
                if midE!=(0,0):
                    count = 0
                    for i in range(5):
                        if self.matrix[i][0]>midE[0]-10 and self.matrix[i][0]<midE[0]+10 and self.matrix[i][1]>midE[1]-10 and self.matrix[i][1]<midE[1]+10:
                            count += 1
                    if count>2:
                        center = midE
                        break
                fault_tolerance_times = fault_tolerance_times-1

        tts.say("i will change camera id")
        ballDetect.changeCameraId(vd.kBottomCamera)
        posinit.posinit2(0.0,10.0,self.robot_ip,self.robot_port)
        ballDetect.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
        center = ballDetect.getBallData()
        ballDetect.showBallPosition()
        while center[1]<280:
            if center==(0,0):
                ballDetect.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
                center = ballDetect.getBallData()
                ballDetect.showBallPosition()
                print center
                continue
            tts.say("I will go ahead");
            if center[1]<200:
                step=4
            else:
                step=0.5
            moveto.move(self.robot_ip,self.robot_port,step,0,0)
            while (center[1]<280 and center[0] > (wide/2+16)) or (center[0] < (wide/2-16)):
                if center==(0,0):
                    ballDetect.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
                    center = ballDetect.getBallData()
                    ballDetect.showBallPosition()
                    continue
                tts.say("I am checking the coordinate x smaller ")
                print "I am checking the coordinate x smaller"
                #if center[0] > (wide/2+20):
                #    moveto.move(self.robot_ip,self.robot_port,0,-1,0)
                #elif center[0] < (wide/2-20):
                #    moveto.move(self.robot_ip,self.robot_port,0,1,0)
                if center[0] > (wide/2+16):
                    self.motionProxy.changeAngles("HeadYaw",-almath.TO_RAD,0.8)
                elif center[0] < (wide/2-16):
                    self.motionProxy.changeAngles("HeadYaw",almath.TO_RAD,0.8)
                ballDetect.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
                center = ballDetect.getBallData()
                ballDetect.showBallPosition()
                print center
                print "I have checked coordinate x secondly"
        
            angles = self.motionProxy.getAngles("HeadYaw",False)
            self.motionProxy.setAngles("HeadYaw",0,0.5)
            self.motionProxy.moveTo(0.0,0.0,angles[0])
            
            fault_tolerance_times = 2
            while fault_tolerance_times>0:
                for i in range(5):
                    ballDetect.updateBallData(client="xxxx", colorSpace="BGR", fitting=True)
                    self.matrix[i] = ballDetect.getBallData()
                self.matrix = sorted(self.matrix,key=lambda x: (x[1], x[0]))
                #debug 
                string = ""
                for i in range(5):
                    string += str(self.matrix[i])
                print string
                print fault_tolerance_times
                midE = self.matrix[len(self.matrix)-2]
                if midE!=(0,0):
                    count = 0
                    for i in range(5):
                        if self.matrix[i][0]>midE[0]-10 and self.matrix[i][0]<midE[0]+10 and self.matrix[i][1]>midE[1]-10 and self.matrix[i][1]<midE[1]+10:
                            count += 1
                    if count>2:
                        center = midE
                        break
                fault_tolerance_times = fault_tolerance_times-1
            print "I have checked coordinate y secondly"