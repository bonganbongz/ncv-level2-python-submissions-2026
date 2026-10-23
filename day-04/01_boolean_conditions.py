marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 75:
    print("Distinction")
elif marks >= 50:
    print("Pass")
else:
    print("Failed")