#  Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third Number :"))
if a>b:
    print("Greater Number is",a)
elif b>c:
    print("Greater Number is",b)
elif c>a:
    print("Greater Number is",c)
else:
    print("The Number Are Same")