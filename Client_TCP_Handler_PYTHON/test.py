2#Test script to see if we can communicate with RobotStudio on a local machine
#Times how long it takes to form the connection and recieve an acknowledgement

#Have to open the RAPID socket first - then connect

import Client_TCP_Handler_PYTHON.tcp_controller as tcp_controller
import CMD_LIST
import cntrl_scripts

six_axis_tcp = tcp_controller.six_axis_tcp_base("192.168.125.1", 55555, CMD_LIST.VALID_CMDS)

#six_axis_tcp = tcp_controller.six_axis_tcp_base("127.0.0.1", 55555, CMD_LIST.VALID_CMDS)

six_axis_tcp.socket_connect()

print("Connecting to Socket")

cntrl_scripts.latency_test(six_axis_tcp)

six_axis_tcp.socket_close()






