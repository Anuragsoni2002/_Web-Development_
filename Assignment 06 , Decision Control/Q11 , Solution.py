""" Write a python script to take the month value in numeric format and display the number of days in it.
n=int(input("Enter Month Number :-"))
match n:
    case 1:
        print("JANUARY - 30 days")
    case 2:
        print("FEBRUARY - 28 days")
    case 3:
        print("MARCH - 31 days")
    case 4:
        print("APRIL - 30 days")
    case 5:
        print("MAY - 31 days")
    case 6:
        print("JUNE - 30 days")
    case 7:
        print("JULY - 31 days")
    case 8:
        print("AUGUST - 31 days")
    case 9:
        print("SEPTEMBER - 30 days")
    case 10:
        print("OCTOBER - 31 days")
    case 11:
        print("NOVEMBER - 30 days")
    case 12:
        print("DECEMBER - 31 days")
    case  _:
        print("DEFAULT")

"""


month=int(input("Enter month number"))
if month in (1,3,5,7,8,10,12):
    print("31 days")

elif month in (4,6,9,11):
    print("30 days")

elif month==2:
    print("28 or 29 days")

else:
    print("Invalid Month Number")
