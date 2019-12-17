import os
msg=os.sys.argv[1]

for signo in msg:
    if(signo=="*"):
        print("CORRE")
    if(signo=="+"):
        print("ANTES")
    if(signo=="#"):
        print("QUE TE VEAN")
    if(signo=="$"):
        print("Y")
    if(signo=="-"):
        print("TE PIDAN EL DNI")
