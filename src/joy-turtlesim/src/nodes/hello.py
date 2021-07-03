import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

#tutrle_teleop_key displayer/ keyboard arraw keys

def call_back(msg):
    linear = msg.linear.x
    ang = msg.angular.z
    print("z"+str(ang),"x"+str(linear))
    
if __name__== "__main__":

    
    rospy.init_node("key_reader")
    rate = rospy.Rate(20)

    rospy.Subscriber("/turtle1/cmd_vel",Twist,callback=call_back)

    while not rospy.is_shutdown():
        rate.sleep()    