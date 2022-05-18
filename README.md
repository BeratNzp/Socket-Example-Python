# Socket-Example
This project can receive requests from clients as a server via sockets. And its running with TCP Protocols.

### How to turn on server:
``chmod +x server.py``   
``./server.py &``

### How to turn back to terminal:
Press "CTRL+C"   
(Server is still running)

### How to turn off server:   
``socketServerPythonPID=$(ps -ux | grep 'server.py' | awk 'NR==1{print $2}')``   
``kill $socketServerPythonPID``
