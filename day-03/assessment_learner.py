# assessment_learner

test1 = float(input("Enter Test 1 mark (%): "))
test2 = float(input("Enter Test 2 mark (%): "))

icass = (test1 * 0.30) + (test2 * 0.70)

print("Final ICASS mark:", round(icass, 2), "%")

if icass >= 40:
    print("The student qualifies to write the examination.")
else:
    print("The student does not qualify to write the examination.")