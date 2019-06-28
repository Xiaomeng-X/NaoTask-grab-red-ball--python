from naoqi import ALProxy
from naoqi import ALModule

class GrabObj(ALModule):
    def __init__(self,name,robot_ip,robot_port):
        ALModule.__init__(self,name)
        self.motionProxy = ALProxy("ALMotion", robot_ip, robot_port)

    def grab(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[0.00302602, [3, -0.733333, 0], [3, 0.733333, 0]], [0.00302602, [3, -0.733333, 0], [3, 0.533333, 0]], [0.00302602, [3, -0.533333, 0], [3, 0.333333, 0]], [0.00449183, [3, -0.333333, -0.000393328], [3, 0.533333, 0.000629325]], [0.00609397, [3, -0.533333, 0], [3, 0.466667, 0]], [0.00609397, [3, -0.466667, 0], [3, 0.6, 0]], [0.00609397, [3, -0.6, 0], [3, 0.6, 0]], [0.00149202, [3, -0.6, 0], [3, 0.533333, 0]], [0.00302602, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.176453, [3, -0.333333, 0], [3, 0, 0]]])
        
        names.append("HeadYaw") 
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[0.00302602, [3, -0.733333, 0], [3, 0.733333, 0]], [0.00302602, [3, -0.733333, 0], [3, 0.533333, 0]], [0.00302602, [3, -0.533333, 0], [3, 0.333333, 0]], [0.00709235, [3, -0.333333, 0], [3, 0.533333, 0]], [0.00149202, [3, -0.533333, 0], [3, 0.466667, 0]], [0.00149202, [3, -0.466667, 0], [3, 0.6, 0]], [0.00149202, [3, -0.6, 0], [3, 0.6, 0]], [0.00149202, [3, -0.6, 0], [3, 0.533333, 0]], [0.00302602, [3, -0.533333, 0], [3, 0.333333, 0]], [0.00149202, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LAnklePitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-0.34826, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.34826, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.34826, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.34826, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.34826, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.34826, [3, -0.466667, 0], [3, 0.6, 0]], [-0.34826, [3, -0.6, 0], [3, 0.6, 0]], [-0.351328, [3, -0.6, 0], [3, 0.533333, 0]], [-0.34826, [3, -0.533333, -0.00306829], [3, 0.333333, 0.00191768]], [0.0996681, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[0.00464392, [3, -0.733333, 0], [3, 0.733333, 0]], [0.00464392, [3, -0.733333, 0], [3, 0.533333, 0]], [0.00464392, [3, -0.533333, 0], [3, 0.333333, 0]], [0.0135159, [3, -0.333333, 0], [3, 0.533333, 0]], [0.00924586, [3, -0.533333, 0], [3, 0.466667, 0]], [0.00924586, [3, -0.466667, 0], [3, 0.6, 0]], [0.00924586, [3, -0.6, 0], [3, 0.6, 0]], [0.00924586, [3, -0.6, 0], [3, 0.533333, 0]], [0.00464392, [3, -0.533333, 0.00460194], [3, 0.333333, -0.00287621]], [-0.122678, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-0.0551819, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.0413762, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.0413762, [3, -0.533333, 0], [3, 0.333333, 0]], [-1.52856, [3, -0.333333, 0], [3, 0.533333, 0]], [-1.32533, [3, -0.533333, 0], [3, 0.466667, 0]], [-1.32533, [3, -0.466667, 0], [3, 0.6, 0]], [-1.32533, [3, -0.6, 0], [3, 0.6, 0]], [-0.049046, [3, -0.6, 0], [3, 0.533333, 0]], [-0.0551819, [3, -0.533333, 0.00613588], [3, 0.333333, -0.00383493]], [-0.421808, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-1.39445, [3, -0.733333, 0], [3, 0.733333, 0]], [-2.06635, [3, -0.733333, 0], [3, 0.533333, 0]], [-1.16435, [3, -0.533333, -0.330683], [3, 0.333333, 0.206677]], [-0.454269, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.46331, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.46331, [3, -0.466667, 0], [3, 0.6, 0]], [-0.46331, [3, -0.6, 0], [3, 0.6, 0]], [-0.477115, [3, -0.6, 0.0138056], [3, 0.533333, -0.0122716]], [-1.39445, [3, -0.533333, 0], [3, 0.333333, 0]], [-1.21037, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[0.0252, [3, -0.733333, 0], [3, 0.733333, 0]], [0.0252, [3, -0.733333, 0], [3, 0.533333, 0]], [0.83, [3, -0.533333, -0.199959], [3, 0.333333, 0.124974]], [1, [3, -0.333333, 0], [3, 0.533333, 0]], [0.3032, [3, -0.533333, 0], [3, 0.466667, 0]], [0.3032, [3, -0.466667, 0], [3, 0.6, 0]], [0.3032, [3, -0.6, 0], [3, 0.6, 0]], [0.3, [3, -0.6, 0.00319999], [3, 0.533333, -0.00284444]], [0.0252, [3, -0.533333, 0], [3, 0.333333, 0]], [0.2876, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-0.443284, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.443284, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.443284, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.443518, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.443284, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.443284, [3, -0.466667, 0], [3, 0.6, 0]], [-0.443284, [3, -0.6, 0], [3, 0.6, 0]], [-0.444818, [3, -0.6, 0], [3, 0.533333, 0]], [-0.443284, [3, -0.533333, -0.00153415], [3, 0.333333, 0.000958842]], [0.136568, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-0.00149202, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.00149202, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.00149202, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.00409152, [3, -0.333333, 0.00029279], [3, 0.533333, -0.000468464]], [-0.00455999, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.00455999, [3, -0.466667, 0], [3, 0.6, 0]], [-0.00455999, [3, -0.6, 0], [3, 0.6, 0]], [0.00464392, [3, -0.6, 0], [3, 0.533333, 0]], [-0.00149202, [3, -0.533333, 0], [3, 0.333333, 0]], [0.093616, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[4.19617e-05, [3, -0.733333, 0], [3, 0.733333, 0]], [4.19617e-05, [3, -0.733333, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.00335875, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.00302602, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.00302602, [3, -0.466667, 0], [3, 0.6, 0]], [-0.00302602, [3, -0.6, 0], [3, 0.6, 0]], [4.19617e-05, [3, -0.6, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.159494, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[0.691793, [3, -0.733333, 0], [3, 0.733333, 0]], [0.691793, [3, -0.733333, 0], [3, 0.533333, 0]], [0.691793, [3, -0.533333, 0], [3, 0.333333, 0]], [0.692964, [3, -0.333333, -0.000393149], [3, 0.533333, 0.000629039]], [0.694859, [3, -0.533333, 0], [3, 0.466667, 0]], [0.694859, [3, -0.466667, 0], [3, 0.6, 0]], [0.694859, [3, -0.6, 0], [3, 0.6, 0]], [0.694859, [3, -0.6, 0], [3, 0.533333, 0]], [0.691793, [3, -0.533333, 0.00306656], [3, 0.333333, -0.0019166]], [-0.0859461, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[1.41277, [3, -0.733333, 0], [3, 0.733333, 0]], [1.41277, [3, -0.733333, 0], [3, 0.533333, 0]], [0.174835, [3, -0.533333, 0], [3, 0.333333, 0]], [0.191641, [3, -0.333333, -0.0108166], [3, 0.533333, 0.0173065]], [0.259204, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.254818, [3, -0.466667, 0], [3, 0.6, 0]], [-0.254818, [3, -0.6, 0], [3, 0.6, 0]], [0.249999, [3, -0.6, -0.294281], [3, 0.533333, 0.261583]], [1.41277, [3, -0.533333, -0.0859038], [3, 0.333333, 0.0536899]], [1.46646, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[1.23943, [3, -0.733333, 0], [3, 0.733333, 0]], [1.23943, [3, -0.733333, 0], [3, 0.533333, 0]], [0.644238, [3, -0.533333, 0.233835], [3, 0.333333, -0.146147]], [0.0994838, [3, -0.333333, 0], [3, 0.533333, 0]], [0.262272, [3, -0.533333, 0], [3, 0.466667, 0]], [0.262272, [3, -0.466667, 0], [3, 0.6, 0]], [1.32645, [3, -0.6, 0], [3, 0.6, 0]], [1.24557, [3, -0.6, 0.00690366], [3, 0.533333, -0.00613659]], [1.23943, [3, -0.533333, 0.00613659], [3, 0.333333, -0.00383537]], [0.164096, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-0.00157595, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.823801, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.813062, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.85234, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.837606, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.842994, [3, -0.466667, 0], [3, 0.6, 0]], [-0.842994, [3, -0.6, 0], [3, 0.6, 0]], [-0.848343, [3, -0.6, 0], [3, 0.533333, 0]], [-0.00157595, [3, -0.533333, -0.134992], [3, 0.333333, 0.0843698]], [0.0827939, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-0.358915, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.358915, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.358915, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.358915, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.357381, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.357381, [3, -0.466667, 0], [3, 0.6, 0]], [-0.357381, [3, -0.6, 0], [3, 0.6, 0]], [-0.363515, [3, -0.6, 0], [3, 0.533333, 0]], [-0.358915, [3, -0.533333, -0.00460068], [3, 0.333333, 0.00287542]], [0.0874801, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-0.00916195, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.00916195, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.00916195, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.0178491, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.0122299, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.0122299, [3, -0.466667, 0], [3, 0.6, 0]], [-0.0122299, [3, -0.6, 0], [3, 0.6, 0]], [-0.0152981, [3, -0.6, 0], [3, 0.533333, 0]], [-0.00916195, [3, -0.533333, -0.00613618], [3, 0.333333, 0.00383511]], [0.121228, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[0.0567998, [3, -0.733333, 0], [3, 0.733333, 0]], [0.0445281, [3, -0.733333, 0], [3, 0.533333, 0]], [0.0445281, [3, -0.533333, 0], [3, 0.333333, 0]], [1.4591, [3, -0.333333, 0], [3, 0.533333, 0]], [1.31621, [3, -0.533333, 0], [3, 0.466667, 0]], [1.31621, [3, -0.466667, 0], [3, 0.6, 0]], [1.31621, [3, -0.6, 0], [3, 0.6, 0]], [0.046062, [3, -0.6, 0], [3, 0.533333, 0]], [0.0567998, [3, -0.533333, -0.0107378], [3, 0.333333, 0.00671112]], [0.42496, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[1.3959, [3, -0.733333, 0], [3, 0.733333, 0]], [2.0678, [3, -0.733333, 0], [3, 0.533333, 0]], [1.16733, [3, -0.533333, 0.324938], [3, 0.333333, -0.203086]], [0.483725, [3, -0.333333, 0], [3, 0.533333, 0]], [0.496974, [3, -0.533333, 0], [3, 0.466667, 0]], [0.496974, [3, -0.466667, 0], [3, 0.6, 0]], [0.496974, [3, -0.6, 0], [3, 0.6, 0]], [0.486237, [3, -0.6, 0], [3, 0.533333, 0]], [1.3959, [3, -0.533333, 0], [3, 0.333333, 0]], [1.21182, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[0.0192, [3, -0.733333, 0], [3, 0.733333, 0]], [0.0192, [3, -0.733333, 0], [3, 0.533333, 0]], [0.83, [3, -0.533333, -0.20119], [3, 0.333333, 0.125744]], [1, [3, -0.333333, 0], [3, 0.533333, 0]], [0.304, [3, -0.533333, 0], [3, 0.466667, 0]], [0.304, [3, -0.466667, 0], [3, 0.6, 0]], [0.304, [3, -0.6, 0], [3, 0.6, 0]], [0.3, [3, -0.6, 0.00399998], [3, 0.533333, -0.00355554]], [0.0192, [3, -0.533333, 0], [3, 0.333333, 0]], [0.2852, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-0.44797, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.44797, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.44797, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.448208, [3, -0.333333, 0.000237388], [3, 0.533333, -0.00037982]], [-0.457173, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.457173, [3, -0.466667, 0], [3, 0.6, 0]], [-0.457173, [3, -0.6, 0], [3, 0.6, 0]], [-0.454105, [3, -0.6, -0.00162408], [3, 0.533333, 0.00144363]], [-0.44797, [3, -0.533333, -0.00613482], [3, 0.333333, 0.00383427]], [0.141086, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[4.19617e-05, [3, -0.733333, 0], [3, 0.733333, 0]], [4.19617e-05, [3, -0.733333, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.333333, 0]], [0.00872912, [3, -0.333333, 0], [3, 0.533333, 0]], [0.00617791, [3, -0.533333, 0], [3, 0.466667, 0]], [0.00617791, [3, -0.466667, 0], [3, 0.6, 0]], [0.00617791, [3, -0.6, 0], [3, 0.6, 0]], [4.19617e-05, [3, -0.6, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.091998, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[4.19617e-05, [3, -0.733333, 0], [3, 0.733333, 0]], [4.19617e-05, [3, -0.733333, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.00335875, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.00302602, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.00302602, [3, -0.466667, 0], [3, 0.6, 0]], [-0.00302602, [3, -0.6, 0], [3, 0.6, 0]], [4.19617e-05, [3, -0.6, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.159494, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[0.693411, [3, -0.733333, 0], [3, 0.733333, 0]], [0.693411, [3, -0.733333, 0], [3, 0.533333, 0]], [0.693411, [3, -0.533333, 0], [3, 0.333333, 0]], [0.694576, [3, -0.333333, 0], [3, 0.533333, 0]], [0.684206, [3, -0.533333, 0], [3, 0.466667, 0]], [0.684206, [3, -0.466667, 0], [3, 0.6, 0]], [0.684206, [3, -0.6, 0], [3, 0.6, 0]], [0.693411, [3, -0.6, 0], [3, 0.533333, 0]], [0.693411, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.0889301, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[1.43893, [3, -0.733333, 0], [3, 0.733333, 0]], [1.43893, [3, -0.733333, 0], [3, 0.533333, 0]], [0.173384, [3, -0.533333, 0], [3, 0.333333, 0]], [0.284489, [3, -0.333333, 0], [3, 0.533333, 0]], [0.268493, [3, -0.533333, 0.0159959], [3, 0.466667, -0.0139964]], [-0.254818, [3, -0.466667, 0], [3, 0.6, 0]], [-0.254818, [3, -0.6, 0], [3, 0.6, 0]], [0.227074, [3, -0.6, -0.298897], [3, 0.533333, 0.265686]], [1.43893, [3, -0.533333, -0.0245462], [3, 0.333333, 0.0153414]], [1.45427, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[-1.24258, [3, -0.733333, 0], [3, 0.733333, 0]], [-1.24258, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.644321, [3, -0.533333, -0.224099], [3, 0.333333, 0.140062]], [-0.150098, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.266959, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.266959, [3, -0.466667, 0], [3, 0.6, 0]], [-1.32645, [3, -0.6, 0], [3, 0.6, 0]], [-1.24872, [3, -0.6, -0.00690366], [3, 0.533333, 0.00613659]], [-1.24258, [3, -0.533333, -0.00613659], [3, 0.333333, 0.00383537]], [-0.17185, [3, -0.333333, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.6, 15.2, 16.2])
        keys.append([[0.00916195, [3, -0.733333, 0], [3, 0.733333, 0]], [0.845191, [3, -0.733333, 0], [3, 0.533333, 0]], [0.834454, [3, -0.533333, 0], [3, 0.333333, 0]], [0.87996, [3, -0.333333, 0], [3, 0.533333, 0]], [0.860533, [3, -0.533333, 0], [3, 0.466667, 0]], [0.860533, [3, -0.466667, 0], [3, 0.6, 0]], [0.860533, [3, -0.6, 0], [3, 0.6, 0]], [0.882007, [3, -0.6, 0], [3, 0.533333, 0]], [0.00916195, [3, -0.533333, 0], [3, 0.333333, 0]], [0.0689882, [3, -0.333333, 0], [3, 0, 0]]])

        self.motionProxy.angleInterpolationBezier(names, times, keys)