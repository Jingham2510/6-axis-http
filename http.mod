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
        !Just incase something breaks - panic and close the sockets
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
        VAR num req_len;

        !Strips the first four characters to identify the command
        cmd_ID := StrPart(cmd,1,4);
        !Accesses the request related to the command 
        req_len := StrLen(cmd) - 5;
        cmd_req:=StrPart(cmd,6, req_len);

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
            
            !Request the robot move to a specific position
            CASE "MVTO":
                move_to cmd_req;
            
            !if unprogrammed/unknown command is sent
            DEFAULT:
                SocketSend client_socket\Str:= "UNKNOWN CMD";
            
        ENDTEST

    ENDPROC

    
    !Moves the robot end-affector to a specified posiiton
    PROC move_to(string target_pos)
        !decode the target pos into a robtarget variable
        VAR robtarget rob_trgt_pos;
        VAR num curr_num;
        !There are 17 values in one robot target
        CONST num vals := 17;
        
        !Array storing the rob target values
        VAR num val_arr{17};
        
        VAR num start_from := 1;
        
        VAR num next_comma_pos;
        VAR string curr_string;
        
        !Split the target_pos string into an array of values
        FOR i FROM 1 TO vals DO                         
            

            !Find the next comma
            next_comma_pos := StrFind(target_pos, start_from + 1, ",");           
            
            !Identify the next string to be converted - stripping the commas
            curr_string := StrPart(target_pos, start_from + 1, next_comma_pos - start_from - 1);
            
            TPWrite ValToStr(i) + " : " + curr_string;
            
            !Splits the target pos string, and stores it as a number
            StrToVal(curr_string, curr_val);
            
            
            
            !Place the current number into the relevant slot in the value array
            val_arr{i} := curr_num;
            
            !start from the next comma
            start_from := next_comma_pos;
            
            
        ENDFOR
        
        SocketSend client_socket\Str:= "MVTO CONVERTED";
        
        ERROR
            
            !If something breaks
            TPWrite "Invalid target position";
            SocketSend client_socket\Str:= "INVALID POS";
                   
        
        
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