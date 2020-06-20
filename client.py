from mcrcon import MCRcon
import time
import os

savefile = "save.rcon"

def Connect():
    print("RCON Client v1.0.0")
    
    if (os.path.isfile(savefile) == True):
        print("RCON file found! Attempting to connect using file parameters...")
        f = open(savefile, "r")
        data = f.readlines() 
        try:
            para = []
            for d in data:
                para.append(d.strip(' ').strip('\n'))
            return [str(para[0]),int(para[1]),str(para[2])]
        except:
            print("The RCON file is invalid, returning to manual configuration")
    
    address = input("Server Address: ")
    port = input("Server Port: ")
    key = input("Server Password: ")
    
    print("Would you like to save these settings for future use? (Y/n)")
    r = input("")
    if(r == "y" or r == "Y"):
        f = open(savefile, "w")
        f.write("%s\n%s\n%s\n" % (address, port, key))
        print("Saved data to file")
    
    print("Connect to " + str(address) + ":" + str(port) + " using password (" + str(key) + ")? (Y/n)")
    r = input("")
    if(r == "y" or r == "Y"):
        return [address,port,key]
    
        
    
    return None

def main():
    c = None
    while(c == None):
        c = Connect()
    print("Attempting to connect...")
    with MCRcon(c[0],c[2],int(c[1])) as session:
        loop = True
        print("NOTE: To return to manual mode just delete the save.rcon file")
        print("Connection Successful! Do 'help' for a list of commands and 'exit' to close the connection")
        while(loop == True):
            cmd = input("> ")
            if(cmd == "exit"):
                loop = False
                print("Disconnecting from server...")
                session.disconnect()
            else:
                rsp = session.command(cmd)
                print(rsp)
                
    print("Successfully Disconnected! The client will now close")
    exit()
            
main()