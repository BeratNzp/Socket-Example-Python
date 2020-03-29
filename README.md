# Socket-Server-Example
This project can receive requests from clients as a server via sockets.

### How to turn on server:
  ``chmod +x mp-server.py``
  ``./mp-server.py &``

### How to turn back to terminal:
Press CTRL+X"

(Server is still running)

### How to turn off server:**
Learn "PID number" of your server with this command:

  ``ps -ux | grep 'mp-server.py' | awk 'NR==1{print $2}'``
  
Then

  ``kill "PID number"``
