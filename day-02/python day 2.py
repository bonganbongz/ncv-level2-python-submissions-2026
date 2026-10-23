A = int(input("first number: "))
B = int(input("second number: "))

if A < B:
    factor = A
else:
    factor = B
        
while A % factor !=0 or B % factor != 0:
    factor = factor - 1
            
print("The highest common factor is", factor)