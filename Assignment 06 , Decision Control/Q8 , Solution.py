# Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
a=int(input("Enter Value A of a Quadratic Equation :"))
b=int(input("Enter Value B of a Quadratic Equation :"))
c=int(input("Enter Value C of a Quadratic Equation :"))
# formula - d=b**2-4ac  #d=discriminant

d=b**2-4*a*c
if d>0:
    print("Real and Distinct roots",d)
elif d==0:
    print("Real and Equal roots",d)
else:
    print("Imaginary roots",d)