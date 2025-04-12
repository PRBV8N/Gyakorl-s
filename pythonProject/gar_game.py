b=False
while True:
    a=input("> ").lower()
    if a=="help":
        print("Start-start the car, Stop-stop the car, Quit-exit the game")
    elif a=="start" and b==False:
        print("Car started")
        b = True
    elif a=="start" and b==True:
        print("Car already started")
    elif a=="stop" and b==True:
        print("Car stopped")
        b=False
    elif a=="stop" and b==False:
        print("Car is not moving")
    elif a=="quit":
        print("Exit")
        break
    else:
        print("IDK")
