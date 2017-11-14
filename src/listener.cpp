#include "ros/ros.h"
#include "baxter_core_msgs/JointCommand.h"
#include <sstream>
#include <iostream>
#include "math.h"
int main(int argc, char **argv){

    ros::init(argc, argv, "joint_position_command");
    ros::NodeHandle n;
    ros::Publisher jc_pub = n.advertise<baxter_core_msgs::JointCommand>("/robot/limb/right/joint_command", 1);
    ros::Rate loop_rate(10);
    baxter_core_msgs::JointCommand jc_msg;
    jc_msg.mode = jc_msg.POSITION_MODE;


    jc_msg.names.push_back("right_s0");
    jc_msg.names.push_back("right_s1");
    jc_msg.names.push_back("right_w0");
    jc_msg.names.push_back("right_w1");
    jc_msg.names.push_back("right_w2");
    jc_msg.names.push_back("right_e0");
    jc_msg.names.push_back("right_e1");

    jc_msg.command.insert(jc_msg.command.begin(),0.0);
    jc_msg.command.push_back(0.0);
    jc_msg.command.push_back(0.0);
    jc_msg.command.push_back(0.0);
    jc_msg.command.push_back(0.0);
    jc_msg.command.push_back(0.0);
    jc_msg.command.push_back(1.0);


    while (ros::ok())
    {

        jc_pub.publish(jc_msg);
        ros::spinOnce();
        loop_rate.sleep();
    }
  return 0;
}
