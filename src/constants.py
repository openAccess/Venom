ttyUSB_USB2DYNAMIXEL = "/dev/ttyUSB1"

# DXL_LIB_PATH = "/home/chinmay/DynamixelSDK/c/build/linux64/libdxl_x64_c.so"
DXL_LIB_PATH = "/home/carnage/DynamixelSDK/c/build/linux64/libdxl_x64_c.so"



ENABLE_DXL_MESSAGES = False

# Servo Props
servoId = [9,18,11,16,2,3,12,13,17,14,8,1]
SERVO_RES = 0.2932551319648094

#Set-Point of Each Servo
FixedPoints = [516+153.45,512,515,
               810-153.45,495,210,
               512+153.45,512,515,
               512-153.45,512,819]  
# Direction of Motion
dirVector = [-1,1,1,
              1,1,1,
              1,-1,-1,
              -1,-1,-1]

# Venom Props

linkLength = [5.5,0,8.3,14.1]
# linkLength = [1,0,1,1]

# Reference Constants
A = 0
B = 1
C = 2
D = 3
TOP = 0
MIDDLE = 1
BOTTOM = 2

CREEP = 0
TROT = 1