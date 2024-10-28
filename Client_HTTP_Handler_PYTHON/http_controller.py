"""
HTTP Controller Class
Acts as the connection between the python code and the RAPID HTTP base
Allows for sending commands to the 6-axis robot

"""

import socket


class six_axis_http_base():

    """
    Standard __init__ function
    
    Keyword Args:
        ip - The IP the socket will be related to
        port - The port the socket will be related to
        valid_CMD_dict - A dictionary containing the valid commands to send over the HTTP connection
    """
    def __init__(self, ip, port, valid_CMD_dict):
        self.ip = ip
        self.port = port
        self.valid_CMDs = valid_CMD_dict
        
        self.connected = 0
        #Create the socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    """
    Attempts to connect to the socket

    Returns:
        1 - if connection succesful
        -1 - if ocnnection unsuccesful

    """
    def socket_connect(self):

        try:
            self.socket.connect((self.ip, self.port))
            self.connected = 1
            return 1
        except:
            print("CONNECTION FAILED")
            return -1
        

    """
    Attempts to send a request to the connected socket and returns the response
    
    Keyword Args:
        req - The request that is sent to the socket

    Returns:
            The response from the socket (if there is one)
            Otherwise it returns the error message

            -1 - SOCKET TX/RX ERROR
            -2 - INVALID COMMAND
            -3 - NOT CONNECTED TO SOCKET

    """
    def request_resp(self, req):
        #Ensure their is a socket to send the request to
        if self.connected:
            
            #Check the command is valid
            valid_cmd = self._CMD_check(req[:4])

            if valid_cmd:
                try:
                    #Send the request and recieve the response
                    self.socket.send(bytes(req,"UTF-8"))
                    resp = self.socket.recv(4096).decode("UTF-8")

                    return resp

                except Exception as e:
                    print(e)

                    print("ERROR - SOCKET ERROR")
                    return -1



            else:
                print("WARNING: Invalid CMD")
                return -2


        else:
            print("WARNING: Socket not connected")
            return -3




    """
    Attempts to send a request to the connected socket  - does not expect response
    
    Keyword Args:
        req - The request that is sent to the socket

    Returns:
            Returns an error code if there is an error            
            -1 - SOCKET TX/RX ERROR
            -2 - INVALID COMMAND
            -3 - NOT CONNECTED TO SOCKET

    """
    def request(self, req):
        #Ensure their is a socket to send the request to
        if self.connected:
            
            #Check the command is valid
            valid_cmd = self._CMD_check(req[:4])

            if valid_cmd:
                try:
                    #Send the request and recieve the response
                    self.socket.send(bytes(req,"UTF-8"))

                    return 1

                except:
                    print("ERROR - SOCKET ERROR")
                    return -1



            else:
                print("WARNING: Invalid CMD")
                return -2


        else:
            print("WARNING: Socket not connected")
            return -3





    """
    Closes the socket connection

    Returns:
        1 - Socket succesfully closed    
    """
    def socket_close(self):

        #Tell the host to close the socket as well
        self.request("CLOS:1")
        
        self.socket.close()
        self.connected = 0

        return 1





    """
    Checks if a command is valid (internal to class)

    Keyword Args:
        CMD - The four letter CMD word

    Returns:
        1 - if the CMD is valid
        0 - if the CMD is invalid
    """
    def _CMD_check(self, CMD):
       

        if any(x for x in self.valid_CMDs if x["CMD"] == CMD):
            return 1
        
        else:
            return 0
