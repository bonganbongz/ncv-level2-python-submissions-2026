# 09_list_operations

marks = []

mark = int(input("Enter mark (-1 to stop): "))

while mark != -1:
    marks.append(mark)
    mark = int(input("Enter mark (-1 to stop): "))

print(f"Our list has {len(marks)} elements")
print(marks)