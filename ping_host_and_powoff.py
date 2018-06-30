import os
import time
j=0
while 1:
    val=os.popen('ping -c 1 192.168.80.133|grep icmp_seq=|awk \'{ print $6 }\'').read().strip().replace('\n',"")
    if val=='Unreachable':
        j+=1
    else:
        j=0
    if j==10:
        os.popen("poweroff")
    print(val)
    print(j)
    time.sleep(5)