2#Test script to see if we can communicate with RobotStudio on a local machine
#Times how long it takes to form the connection and recieve an acknowledgement

#Have to open the RAPID socket first - then connect

import http_controller
import CMD_LIST
import matplotlib.pyplot as plt
import numpy as np
import random

six_axis_http = http_controller.six_axis_http_base("127.0.0.1", 55555, CMD_LIST.VALID_CMDS)



six_axis_http.socket_connect()

print("Connecting to Socket")


"""
#Joint set tester
test_jnt_a = "[[0, 45, 45, 0, 45, 0], [9E9, 9E9, 9E9, 9E9, 9E9, 9E9]]"

test_jnt_b = "[[20, 45, 45, 0, 45, 0], [9E9, 9E9, 9E9, 9E9, 9E9, 9E9]]"


test_jnts = [test_jnt_a, test_jnt_b]

for x in test_jnts:
    resp = six_axis_http.request_resp(f"STJT:{x}")
    print(resp)

"""

z_delta = 5

pos_info = []
real_force_info = []


rand_force_info = [random.randint(1, 100) for i in range(100)]

for i in range(100):
    six_axis_http.request(f"MVTL:0000 0000 -00{z_delta}")

    pos_info.append((six_axis_http.read_port()).strip("[]").split(","))

    real_force_info.append(np.linalg.norm((six_axis_http.read_port()).strip("[]").split(",")))

    


#input(f"Press Enter to continue...")

six_axis_http.socket_close()


#Normalise the force
max_force = max(rand_force_info)
normalised_force = []

for i in range(len(rand_force_info)):

    normalised_force.append(rand_force_info[i]/max_force)


fig = plt.figure()
ax = fig.add_subplot(111, projection ="3d")

x = [float(pos[0]) for pos in pos_info]
y = [float(pos[1]) for pos in pos_info]
z = [float(pos[2]) for pos in pos_info]


scatter = ax.scatter(x, y, z, c = plt.cm.inferno(normalised_force))

fig.colorbar(scatter)

plt.show()



"""
test_pos = "[[1000,200,1000],[0.5,0,0.86603,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]]"

"""


