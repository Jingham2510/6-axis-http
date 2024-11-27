"""
THIS EXISTS PURELY AS DOCUMENTATION/CHECKING TO ENSURE A COMMAND EXISTS
"""

#Echo message command
ECHO = {
    "CMD" : "ECHO",
    "format" : "ECHO:[Message you wish to bounce back]",
    "explanation" : "Requests that the host socket repeats the message back to the client"
}


#Close Socket Command
CLOS = {
    "CMD" : "CLOS",
    "format" : "CLOS:[x] - where x is the close code (atm it doesn't matter)",
    "explanation" : "Requests the host socket to close the connection"
}


#Move to command
MVTO = {
    "CMD" : "MVTO",
    "format" : "MVTO:[[x,y,z], [q1,q2,q3,q4] , [cf1,cf4,cf6,cfx] , [eax_a,eax_b,eax_c,eax_d,eax_e,eax_f]]",
    "explanation": "Requests the robot move to a robtarget defined by the string"

}

#Set joints Command
STJT = {
    "CMD" : "STJT",
    "format" : "STJT:[[ax1, ax2, ax3, ax4, ax5, ax6], [eax_a, eax_b, eax_c, eax_d, eax_e, eax_f]]",
    "explanation" : "Requests the robot modifies its joint angles to the requested angles"
}

#Move the tool relative to it's current position
MVTL = {
    "CMD" : "MVTL",
    "format" : "MVTL:[xxxx yyyy zzzz]",
    "explanation" : "Moves the toolframe from its relative position"

}




VALID_CMDS = [ECHO, CLOS, MVTO, STJT, MVTL]