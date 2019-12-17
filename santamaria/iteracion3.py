#Iteración3

import os
msg=os.sys.argv[1]

for signo in msg:
    if(signo=="*"):
        print("TE VEO")
    if(signo=="+"):
        print("EN LA ESQUINA")
    if(signo=="#"):
        print("SALIENDO")
    if(signo=="$"):
        print("DE LA UNIVERSIDAD")
