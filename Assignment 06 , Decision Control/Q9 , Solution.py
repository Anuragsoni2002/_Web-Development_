#  Write a python script to check whether a given year is a leap year or not.
year=int(input("Enter a Year to check leap year or not :"))
if year%400==0 or year%100!=0 and year%4==0:
    print("Leap Year")
else:
    print("Not Leap Year")
