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




VALID_CMDS = [ECHO, CLOS]