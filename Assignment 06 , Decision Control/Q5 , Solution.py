# Write a python script to print two given words in dictionary order
a=input("Enter First Word :")
b=input("Enter Second Word :")
if a<b:
    print(a,b)
if a>b:
    print(b,a)

# print((b,a) if a>b else (a,b))