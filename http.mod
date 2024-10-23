MODULE http

    !Variables to store socket info and socket commands
    VAR socketdev server_socket;
    VAR socketdev client_socket;
    VAR string receive_string;
    VAR string client_ip;

    PROC main()
        !Open the local socket
        open_local_socket;

        TPWrite "Sockets open";

        accept_socket;

        ! Waiting for a connection request
        WHILE TRUE DO
            !Recieve the string
            SocketReceive client_socket\Str:=receive_string;
            !Process the command
            cmd_handler receive_string;

        ENDWHILE
    ERROR
        RETRY;
    UNDO

        close_sockets;

    ENDPROC


    !Procedure to open the localhost socket - a default ip etc.
    PROC open_local_socket()

        SocketCreate server_socket;
        SocketBind server_socket,"127.0.0.1",55555;
        SocketListen server_socket;

    ENDPROC

    !Accepts a socket connection
    PROC accept_socket()
        SocketAccept server_socket,client_socket\ClientAddress:=client_ip\Time:=WAIT_MAX;
    ENDPROC


    !Handles Commands
    PROC cmd_handler(string cmd)

        VAR string cmd_ID;
        VAR string cmd_req;

        !Strips the first four characters to identify the command
        cmd_ID := StrPart(cmd,1,4);
        !Accesses the actual request related to the command 
        cmd_req:=StrPart(cmd,6,StrLen(cmd)-4);

        TPWrite "ID:"+cmd_ID;
        TPWrite "Request: "+cmd_req;

        !Match case the currently programmed commands
        TEST cmd_ID
            
            
            CASE "ECHO":
                !Repeats the string back to the controller
                SocketSend client_socket\Str:="ECHO_MSG: "+cmd_req;    
            
            !Close the sockets (should fix opening multiple similar sockets)
            CASE "CLOS":
                SocketSend client_socket\Str:= "CLOSING PORT";
                close_sockets;
            
            !if unprogrammed/unknown command is sent
            DEFAULT:
                SocketSend client_socket\Str:= "UNKNOWN CMD";
            
        ENDTEST

    ENDPROC





    !Procedure to close the sockets
    PROC close_sockets()
        !Close the sockets - inform the console
        SocketClose server_socket;
        SocketClose client_socket;
        TPWrite "Sockets Closed";
        !Exit the program
        EXIT;
        
    ENDPROC

ENDMODULE