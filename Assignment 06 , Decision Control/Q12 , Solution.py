# . Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part.
n=complex(input("Enter a Complex Number :"))
if n.real>n.imag:
    print("Real Part is greater")
    print("%d is real Part"%(n.real))
    print()
elif n.real<n.imag:
    print("Imaginary Part is greater")
    print("%d is Imaginary part"%(n.imag))
    print()
else:
    print("boths are equal")
    print()