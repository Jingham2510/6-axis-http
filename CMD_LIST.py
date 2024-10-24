"""
THIS EXISTS PURELY AS DOCUMENTATION/CHECKING TO ENSURE A COMMAND EXISTS
"""

#Echo message command
ECHO = {
    "format" : "ECHO:[Message you wish to bounce back]",
    "explanation" : "Requests that the host socket repeats the message back to the client"
}


#Close Socket Command
CLOS = {
    "format" : "CLOS:[x] - where x is the close code (atm it doesn't matter)",
    "explanation" : "Requests the host socket to close the connection"
}


#Move to command
MVTO = {
    "format" : "MVTO:[[x,y,z], [q1,q2,q3,q4] , [cf1,cf4,cf6,cfx] , [eax_a,eax_b,eax_c,eax_d,eax_e,eax_f]]",
    "explanation": "Requests the robot move to a robtarget defined by the string"

}

#Joint Set Command
JTST = {
    "format" : "JTST:[[ax1, ax2, ax3, ax4, ax5, ax6], [eax_a, eax_b, eax_c, eax_d, eax_e, eax_f]]",
    "explanation" : "Requests the robot modifies its joint angles to the requested angles"
}



VALID_CMDS = [ECHO, CLOS, MVTO]