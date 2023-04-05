print("find the leap year....")
year = int(input("enter the year you want to find it is the leap year or not :"))
if year % 4 == 0:
    if year % 100 != 0:
        print("a leap year...")
    else:
        if year % 400 == 0:
            print("it is a leap yeAR..")
        else:
            print("not a leap year..")
else:
    print("not a leap year...")
