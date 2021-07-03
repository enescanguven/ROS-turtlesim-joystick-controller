import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

#controlling turtlesim 

#global x_ax
x_ax = 0


#global z_ang
z_ang = 0

def joy_callback(Joy):
    
    global x_ax
    x_ax = Joy.axes[1]
    global z_ang
    z_ang= Joy.axes[3]
    
    print("x = "+str(x_ax),"y = "+str(z_ang))

if __name__ == "__main__":

    rospy.init_node("joy")
    
    rospy.Subscriber("/joy", Joy, joy_callback, queue_size=10)


    ack_pub = rospy.Publisher("/turtle1/cmd_vel", Twist,)

    rate = rospy.Rate(20)

    while not rospy.is_shutdown():

        yon = Twist()

        
        yon.angular.z= z_ang*5
        
        yon.linear.x = x_ax*5
        ack_pub.publish(yon)
        rate.sleep()
