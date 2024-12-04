"""
A collection of control scripts
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import time

"""
Move the robot up and measure the force exerted on it
Plots the movement and force relation
TODO: update os its not a random force
"""
def move_up_measure_force(tcp):

    z_delta = 5

    pos_info = []
    real_force_info = []


    rand_force_info = [random.randint(1, 100) for i in range(100)]

    for i in range(100):
        tcp.request(f"MVTL:0000 0000 -00{z_delta}")

        pos_info.append((tcp.read_port()).strip("[]").split(","))

        real_force_info.append(np.linalg.norm((tcp.read_port()).strip("[]").split(",")))


        
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
Test the ability to move between two sets of joint angles
"""
def joint_test(tcp):

    #Joint set tester
    test_jnt_a = "[[0, 45, 45, 0, 45, 0], [9E9, 9E9, 9E9, 9E9, 9E9, 9E9]]"

    test_jnt_b = "[[20, 45, 45, 0, 45, 0], [9E9, 9E9, 9E9, 9E9, 9E9, 9E9]]"


    test_jnts = [test_jnt_a, test_jnt_b]

    for x in test_jnts:
        resp = tcp.request_resp(f"STJT:{x}")
        print(resp)


"""
Test the latency between sending a command and recieving its response
"""
def latency_test(tcp):

    test_str = "LATENCYTEST"

    total_start = time.time()

    latencies = []
    steps = []

    for i in range(100):
        start_time = time.time()

        resp = tcp.request_resp(f"ECHO:{test_str}")

        time_taken = time.time() - start_time

        latencies.append(time_taken)
        steps.append(i)


    print(f"Total time taken for {i + 1} requests: {time.time() - total_start}")

    print(f"Median time: {np.median(latencies)}")
    print(f"Avg time: {np.average(latencies)}")


    plt.plot(steps, latencies)

    plt.savefig("C:/Users/User/Documents/Results/robot_latency_tests/test_no_op")

    plt.show()




    



