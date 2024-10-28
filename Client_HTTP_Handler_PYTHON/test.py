#Test script to see if we can communicate with RobotStudio on a local machine
#Times how long it takes to form the connection and recieve an acknowledgement

#Have to open the RAPID socket first - then connect

import http_controller
import CMD_LIST
import time


six_axis_http = http_controller.six_axis_http_base("127.0.0.1", 55555, CMD_LIST.VALID_CMDS)



six_axis_http.socket_connect()

print("Connecting to Socket")








test_jnt_a = "[[0, 45, 45, 0, 45, 0], [9E9, 9E9, 9E9, 9E9, 9E9, 9E9]]"

test_jnt_b = "[[20, 45, 45, 0, 45, 0], [9E9, 9E9, 9E9, 9E9, 9E9, 9E9]]"


test_jnts = [test_jnt_a, test_jnt_b]

for x in test_jnts:
    resp = six_axis_http.request_resp(f"STJT:{x}")
    print(resp)






#input(f"Press Enter to continue...")

six_axis_http.socket_close()



"""
test_pos = "[[1000,200,1000],[0.5,0,0.86603,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]]"

"""


