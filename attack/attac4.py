import os

# mbtget needs to be installed

cmd = "mbtget -w6 333 -a 0 -d 192.168.168.7 -p 5020"
# cmd2 = "mbtget -n 10 -a 0 192.168.168.7 -p 502"

for i in range(0, 1000):
    os.system(cmd)

#os.system(cmd2)
