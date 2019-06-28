#-*-encoding:UTF-8-*-

#做处理命令行参数使用
import argparse
import time
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from NavigateToMan import NavigateToMan
from DialogModule import DialogModule
from TargetSearchModule import TargetSearchModule
from NavigateToObj import NavigateToObj
from GrabObj import GrabObj
dialog = None
def main(robot_ip,robot_port,dialog_file):
    """     """
    #we need this broker to beable to construct naoqi module
    #and subscribe to other modules
    #the broker must stay alive until the program exist
    myBroker=ALBroker("myBroker",
                      "0.0.0.0",
                      0,
                      robot_ip,
                      robot_port)
    memory = ALProxy("ALMemory",robot_ip,robot_port)
    global dialog
    dialog = DialogModule("dialog",robot_ip,robot_port,dialog_file)
    tts = ALProxy("ALTextToSpeech",robot_ip,robot_port)
    posture = ALProxy("ALRobotPosture",robot_ip,robot_port)
    navigateController = NavigateToMan("NavigateToMan",robot_ip,robot_port)
    navigateController.doNavigate()
    flag = navigateController.isStopped()
    while flag==False:
        time.sleep(1)
        flag = navigateController.isStopped()
    isSearchOut = None
    targetSearch = None
    navigateToObj = NavigateToObj("NavigateToObj",robot_ip,robot_port)
    grabObj = GrabObj("GrabObj",robot_ip,robot_port)
    while True:
        posture.goToPosture("Stand",0.3)
        message = None
        isSearchOut == False
        dialog.dialogSubscribe()
        message = dialog.getMessage()
        while message == None:
            time.sleep(1)
            message = dialog.getMessage()
        dialog.setMessageNull()
        print "message is : " + message
        if message=="crouch":
            posture.goToPosture("Crouch",0.5)
            time.sleep(5)
            continue
        if message=="sitdomn":
            posture.goToPosture("Sit",0.5)
            time.sleep(5)
            continue
        if message=="standup":
            posture.goToPosture("Stand",0.5)
            time.sleep(5)
            continue
        if message=="redball" or message=="greenball":
            targetSearch = TargetSearchModule("TargetSearchModule",robot_ip,robot_port,message)
            isSearchOut = targetSearch.doSearch()
            print "targetSearch finished"
            if isSearchOut==True :
                navigateToObj.NavigateToBall(message)
                grabObj.grab()
                navigateController.doNavigate()
                flag = navigateController.isStopped()
                while flag==False:
                    time.sleep(1)
                    flag = navigateController.isStopped()
                tts.say("here is your "+message)
            else:
                navigateController.doNavigate()
                flag = navigateController.isStopped()
                while flag==False:
                    time.sleep(1)
                    flag = navigateController.isStopped()
                tts.say("i have not find the "+message)
    dialog.unLoad()

if __name__=="__main__":
    parser=argparse.ArgumentParser()   #创建OptionParser的对象，用于设置命令行参数
    parser.add_argument("--ip",
                        type=str,
                        default="192.168.1.3",
                        help="Robot ip address.")
    parser.add_argument("--port",
                        type=int,
                        default=9559,
                        help="Robot port number.")
    parser.add_argument("--file_path",
                        type=str,
                        default="/var/persistent/home/nao/ExampleDialog_mnc.top",
                        help="Absolute path of the dialog topic file"
                             " (on the robot).")
    args = parser.parse_args()
    main(args.ip,args.port,args.file_path)