started = False
print("Type help if you want to know the controls")

while True:
    user = input(">").lower()
    if user == "help":
        print(
            """
start - to start the car
stop  - to stop the car
quit  - to exit
        """
        )
    elif user == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")

    elif user == "stop":
        if not started:
            print("Car is already stopped...")
        else:
            started = False
            print("Car stopped...")

    elif user == "quit":
        break
    else:
        print("I don't understand that...")
