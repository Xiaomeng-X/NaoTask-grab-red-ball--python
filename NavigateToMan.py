#-*-encoding:UTF-8-*-
from naoqi import ALProxy
from naoqi import ALModule

class NavigateToMan(ALModule):
	def __init__(self,name,robot_ip,robot_port):
		ALModule.__init__(self,name)
		self.motionProxy = ALProxy("ALMotion",robot_ip,robot_port)
		self.postureProxy = ALProxy("ALRobotPosture",robot_ip,robot_port)

	def doNavigate(self):
		print "NavigateToMan doNavigate()"
		self.motionProxy.wakeUp()
		self.postureProxy.goToPosture("Stand",0.1)
		self.stopped = False
		#移动到世界坐标系下原点处
		useSensorValues = False
		currentPosition = self.motionProxy.getRobotPosition(useSensorValues)
		print "robot pos:",currentPosition
		self.motionProxy.moveTo(0,0,0)
		self.stopped = True

	def isStopped(self):
		return self.stopped