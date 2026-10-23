# 10_marks_functions

def getMark():
    marks = []
    mark = int(input("Enter mark (-1 to stop): "))

    while mark != -1:
        marks.append(mark)
        mark = int(input("Enter mark (-1 to stop): "))

    return marks

def print_list_size(marks):
    print(f"Our list has {len(marks)} elements")

def print_marks_size(marks):
    print("Your marks are:", marks)

def get_sum_of_marks(marks):
    total = 0

    for x in range(len(marks)):
        total = total + marks[x]

    return total

def get_average(marks):
    if len(marks) == 0:
        print("No marks were entered")
        return

    total = 0

    for x in range(len(marks)):
        total = total + marks[x]

    avg = total / len(marks)
    print(f"The average of all marks = {avg}")

def determine_highest(marks):
    if len(marks) == 0:
        print("No marks entered yet - Press 1 first")
        return

    highest = marks[0]

    for i in range(len(marks)):
        current_mark = marks[i]

        if current_mark > highest:
            highest = current_mark

    print(f"The highest mark is {highest}")


# Menu
menu = "Press 1: Capturing marks\n"
menu += "Press 2: Check number of marks\n"
menu += "Press 3: To calculate sum of marks\n"
menu += "Press 4: To find the highest mark\n"
menu += "Press 5: To calculate average of marks\n"
menu += "Press -1: To exit\n"

entered_marks = []

while True:
    print(menu)
    choice = int(input("Make a choice: "))

    if choice == 1:
        entered_marks = getMark()
        print_marks_size(entered_marks)

    elif choice == 2:
        print_list_size(entered_marks)

    elif choice == 3:
        calc_sum = get_sum_of_marks(entered_marks)
        print("Sum of all marks =", calc_sum)

    elif choice == 4:
        determine_highest(entered_marks)

    elif choice == 5:
        get_average(entered_marks)

    elif choice == -1:
        print("Thank you for using the App")
        break

    else:
        print("Not on the menu")