from postRequests import app
import uvicorn


while True:
    try:
        uvicorn.run(app,port=8000)
    except KeyboardInterrupt:
        c=input("reboot(Y/N):")
        if c=="y" or c=="Y":
            continue
        elif c=="n" or c=="N":
            print("exiting..")
            break
        else:
            print("exiting..")
            break
