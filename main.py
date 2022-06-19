# greeting countdown
import time

print("\n == Greeting Count Down ==")
print("1.Merry Christmas")
print("2.Happy New Year")
print("3.Happy Easter")
print("E.Exit")
choice = input("Input your choice: ")

while choice != "E" and choice != "e":
    if choice == "1":
        print("\n\tD-Default Counter")
        print("\tS-Set Counter")
        step = input("\tinput type of counter: ")
        if step == "D" or step == "d":
            for i in range(3,0,-1):
                print(i)
                time.sleep(1)
            print("\tMerry Christmas!!!")
        elif step == "S" or step == "s":
            set = int(input("\tSet a start number to count down: "))
            for i in range(set,0,-1):
                print(i)
                time.sleep(1)
            print("\tMerry Christmas!!!")
        else:
            print("Invalid type")
    elif choice == "2":
        print("\n\tD-Default Counter")
        print("\tS-Set Counter")
        stp = input("\tinput type of counter: ")
        if stp == "D" or stp == "d":
            for i in range(3,0,-1):
                print(i)
                time.sleep(1)
            print("\tHappy New Year!!!")
        elif stp == "S" or stp == "s":
            st = int(input("\tSet a start number to count down: "))
            for i in range(st, 0, -1):
                print(i)
                time.sleep(1)
            print("\tHappy New Year!!!")
        else:
            print("Invalid type")
    elif choice == "3":
        print("\n\tD-Default Counter")
        print("\tS-Set Counter")
        steps = input("\tinput type of counter: ")
        if steps == "D" or steps == "d":
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)
            print("\tHappy Easter!!!")
        elif steps == "S" or steps == "s":
            sets = int(input("\tSet a start number to count down: "))
            for i in range(sets, 0, -1):
                print(i)
                time.sleep(1)
            print("\tHappy Easter!!!")
        else:
            print("Invalid type")
    else:
        print("Invalid input")

    print("\n == Greeting Count Down ==")
    print("1.Merry Christmas")
    print("2.Happy New Year")
    print("3.Happy Easter")
    print("E.Exit")
    choice = input("Input your choice: ")