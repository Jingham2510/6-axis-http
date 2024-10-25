#Test script to see if we can communicate with RobotStudio on a local machine
#Times how long it takes to form the connection and recieve an acknowledgement

#Have to open the RAPID socket first - then connect

import http_controller
import CMD_LIST
import time


six_axis_http = http_controller("127.0.0.1", 55555, CMD_LIST.VALID_CMDS)



six_axis_http.socket_connect()

print("Connecting to Socket")


test_jnts = "[[-90, 45, -45, 0, 0, 0], [9E9, 9E9, 9E9, 9E9, 9E9, 9E9]]"

resp = six_axis_http.request_resp(f"STJT:{test_jnts}")

print(resp)


input("Press Enter to continue...")

six_axis_http.socket_close()



"""
test_pos = "[[1000,200,1000],[0.5,0,0.86603,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]]"

"""

