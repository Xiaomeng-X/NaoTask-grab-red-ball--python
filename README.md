# NaoTask-grab-red-ball--python
包括内置语音模块的调用、短视野范围目标搜寻模块，短距离导航模块、姿态调整、抓取模块，其中视觉识别部分主要用到了opencv的霍夫圆检测函数

![IMAGE1](https://github.com/Xiaomeng-X/NaoTask-grab-red-ball--python/blob/master/NAO开发思维导图.png)
一、语音对话模块：DialogModule.py 说明：该模块主要调用了nao的内置对话的api，包括一些重要函数

1、topic的加载、激活、对话引擎的启动和卸载、解除激活、引擎的停止，这些部分分别调用了6个函数 dialog = ALProxy("ALDialog", robot_ip, robot_port) 1）topic = dialog.loadTopic(self.file_path.encode('utf-8')) 2）dialog.activateTopic(topic) 3）dialog.subscribe("target") 4）dialog.unloadTopic(topic) 5）dialog.deactivateTopic(topic) 6）dialog.unsubscribe("target")

2、该模块的第二个重点是监测事件和编写回调函数 1）在激活对话模块时编写监测事件的代码，并声明回调函数： memory = ALProxy("ALMemory",robot_ip,robot_port) memory.subscribeToEvent("Dialog/Answered","dialog","getAnswered") 2）在回调函数中编写自定义代码，并且解除对话模块的激活状态 def getAnswered(self,key,value,message): """callback函数""" # 将正则表达式编译成Pattern对象,使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None print "DialogModule getAnswered" pattern = re.compile(r'ALMemory') match = pattern.search(value) if match: self.object_name = memory.getData("object_name") print self.object_name memory.removeData("object_name") memory.unsubscribeToEvent("Dialog/Answered","dialog") # Deactivate topic dialog.deactivateTopic(self.topic) # stop engine dialog.unsubscribe("target")

二、短视野目标搜索模块：TargetSearchModule.py 说明：该模块在一定范围内检索目标是否处于该搜索范围内，包括头部转动搜索和移动小步位移搜索，移动位移搜索内含头部转动搜索；若查找成功，则更加查找目标的位置调整移动方向。

头部搜索：doHeadSearch()方法 移动距离搜索：doSearch()方法

三、短距离导航模块：NavigateToObj.py 说明：该模块在目标搜索模块查找成功后运行，根据视觉检测到的obj在画面中的位置，确定是否向前移动和调整位移方向。该模块包含两个摄像头的应用。远距离时调用上面的摄像头获取实时图像，当物体在图像上的位置超过设定阈值时，则切换到下面的摄像头继续近距离的识别。

远距离： ballDetect.changeCameraId(vd.kTopCamera) ballDetect.updateBallData() center = ballDetect.getBallData() while center[1]<430: moveto.move(self.robot_ip,self.robot_port,step,0,0) while (center[0] > (wide/2+50)) or (center[0] < (wide/2-50)): if center[0] > (wide/2+30): moveto.move(self.robot_ip,self.robot_port,0,-4,0) elif center[0] < (wide/2-30): moveto.move(self.robot_ip,self.robot_port,0,4,0) tts.say("i will change camera id") 近距离： ballDetect.changeCameraId(vd.kBottomCamera) while center[1]<160: moveto.move(self.robot_ip,self.robot_port,1,0,0) while (center[0] > (wide/2+30)) or (center[0] < (wide/2-30)): if center[0] > (wide/2+30): moveto.move(self.robot_ip,self.robot_port,0,-1,0) elif center[0] < (wide/2-30): moveto.move(self.robot_ip,self.robot_port,0,1,0)

四、抓取模块：GrabObj.py 说明：使用choregraphe设计动作动画，并将时间轴产生的关节插值拷贝出来，填充names,times,keys列表数据，并使用贝塞尔曲线函数调用该动作 names = list() times = list() keys = list() motion.angleInterpolationBezier(names, times, keys)

五、视觉模块：VisualTask.py 说明：基于颜色分割图像，设置阈值，将单通道图像转化为二值图像，对二值图像做一个高斯模糊，使用霍夫圆检测函数提取多个圆构成的数组，遍历数组并提取最适合的圆作为正确检测对象，并获取该对象在图像中的位置

例如：提取红色小球 cameraProxy = ALProxy("ALVideoDevice", self.IP, self.PORT) cameraProxy.setActiveCamera(self.cameraId) videoClient = self.cameraProxy.subscribe() frame = cameraProxy.getImageRemote(videoClient) cameraProxy.unsubscribe(videoClient)

self.frameWidth = frame[0] self.frameHeight = frame[1] self.frameChannels = frame[2] self.frameArray = np.frombuffer(frame[6], dtype=np.uint8).reshape([frame[1],frame[0],frame[2]])

channelR = self.frameArray[:,:,2] channelR[channelR<150] = 0 channelR[channelR>255] = 255 channelR = cv2.GaussianBlur(channelR, (9,9), 1.5) grayFrame = np.uint8(np.round(channelR)) circles = self.__findCircles(grayFrame, minDist, minRadius, maxRadius) circle = self.__selectCircle(circles) self.ballData = {"centerX":circle[0][0], "centerY":circle[0][1], "radius":circle[0][2]}
