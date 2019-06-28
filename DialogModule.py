#-*-encoding:UTF-8-*-
#做处理命令行参数使用
import argparse
import time
import re
from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker
dialog = None
class DialogModule(ALModule):  #创建自己的模块，所有的模块都来自almodule
    "A simple module able to react to facedetection events"
    def __init__(self,name,robot_ip,robot_port,file_path):
        ALModule.__init__(self,name)   #创建自己模块的时候把集模块顺便一块初始化
        self.memory = ALProxy("ALMemory",robot_ip,robot_port)
        self.dialog = ALProxy("ALDialog", robot_ip, robot_port)
        self.dialog.setLanguage("Chinese")
        self.file_path = file_path.decode('utf-8')
        self.topic = self.dialog.loadTopic(self.file_path.encode('utf-8'))
        self.robot_ip = robot_ip
        self.robot_port = robot_port
        self.message = None

    def getMessage(self):
        return self.message

    def setMessageNull(self):
        self.message = None

    def dialogSubscribe(self):
        print "DialogModule dialogSubscribe()"
        # Start dialog
        self.dialog.subscribe("target")
        # Activate dialog
        self.dialog.activateTopic(self.topic)
        """
        Few notes:
        Make sure to use a global variable for the module instance.
        Make sure the name you pass to the constructor of ALModule matches the name of your variable.
        The method of your class are automatically transform into bound methods, providing that you wrote a doc string for this method, and it does not start with an underscore.
        """
        self.memory.subscribeToEvent("Dialog/Answered","dialog","getAnswered")
        
    def getAnswered(self,key,value,message):
    	"""callback函数"""
        # 将正则表达式编译成Pattern对象,使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        print "DialogModule getAnswered"
        pattern = re.compile(r'ALMemory')
        match = pattern.search(value)
        if match:
        	self.message = self.memory.getData("dialog_message")
        	print self.message
        	self.memory.removeData("dialog_message")
        	self.memory.unsubscribeToEvent("Dialog/Answered","dialog")
        	# Deactivate topic
        	self.dialog.deactivateTopic(self.topic)
        	# Unload topic
        	self.dialog.unsubscribe("target")

    def unLoad(self):
        self.dialog.unloadTopic(self.topic)


class DialogController(object):
	"""docstring for DialogController"""
	def __init__(self, robot_ip,robot_port,dialog_file):
		super(DialogController, self).__init__()
		global dialog
		dialog = DialogModule("dialog",robot_ip,robot_port,dialog_file)

	def dialogSubscribe(self):
		global dialog
		dialog.dialogSubscribe()

	def getMessage(self):
		global dialog
		dialog.getMessage()

	def setMessageNull(self):
		global dialog
		dialog.setMessageNull()

	def updateDialogVar(self):
		global dialog
		return dialog
		

def control(robot_ip,robot_port,dialog_file):
	global dialog
	dialog = DialogModule("dialog",robot_ip,robot_port,dialog_file)
	dialog.dialogSubscribe()
	while True:
		time.sleep(1)

if __name__=="__main__":
    parser=argparse.ArgumentParser()   #创建OptionParser的对象，用于设置命令行参数
    parser.add_argument("--ip",
                        type=str,
                        default="127.0.0.1",
                        help="Robot ip address.")
    parser.add_argument("--port",
                        type=int,
                        default=49259,
                        help="Robot port number.")
    parser.add_argument("--file_path",
                        type=str,
                        default="/Users/xxmeng/Projects/NAORobots/py/ExampleDialog_mnc.top",
                        help="Absolute path of the dialog topic file"
                             " (on the robot).")

    args = parser.parse_args()
    myBroker=ALBroker("myBroker",
                      "0.0.0.0",
                      0,
                      args.ip,
                      args.port)
    controller = DialogController(args.ip,args.port,args.file_path)
    controller.dialogSubscribe()
    while True:
		time.sleep(1)