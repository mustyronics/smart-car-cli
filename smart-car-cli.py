# I want to make a smart car, where you park a car
# Remove it from garage to drive
# Tell it to drive or stop
# Can't move if it's park
# Can't drive if its already driving and same with stop and parking

def instructions():
    print("\n1. Type 'Drive out' to drive car out")
    print("2. Type 'Move' to start moving car")
    print("3. Type 'Stop' to stop car")
    print("4. Type 'Park' to park car")
    print("5. Type 'exit' to finish\n")


is_parked = True
motion_status = False

while True:
    instructions()
    command = input("What do  you want to do? ").lower()
    if command == "exit":
        print("Hope you have a great time playing, bye!")
        break
    while True:
        if is_parked is True:
            if command == "drive out":
                is_parked = False
                print("Car's ready to move")
                break
            elif command == "move":
                print("The car's parked, drive out first!")
                break
            elif command == "stop":
                print("The car's parked, and not moving!")
                break
            elif command == "park":
                print("The car is parked already")
                break
            else:
                print("This is not a command I understand")
                print("Please choose a command from the instructions below")
                break
        elif is_parked is False:
            if command == "move":
                if motion_status == False:
                    print("Car is now moving")
                    motion_status = True
                    break
                elif motion_status is True:
                    print("The car is already in motion")
                    break
            elif command == "stop":
                if motion_status is True:
                    print("Car has stopped")
                    motion_status = False
                    break
                elif motion_status is False:
                    print("The car has stopped already")
                    break
            elif command == "park":
                if motion_status is True:
                    print("Stop car first")
                    break
                elif motion_status is False:
                    if is_parked is True:
                        print("The car is parked already")
                        break
                    elif is_parked is False:
                        print("Car's parked")
                        is_parked = True
                        break
