name = input("Enter student name: ")
marks = list(map(int, input("Input: ").split()))
total = sum(marks)
avg = total/len(marks)
if 90<=avg<=100:
    grade = "A Grade"
elif 80<=avg<=89:
    grade = "B Grade"
elif 70<=avg<=79:
    grade = "C Grade"
elif 60<=avg<=69:
    grade = "D Grade"
else:
    grade = "F Grade"
my_dict = {"Name":name,
           "Marks":marks,
           "Total marks" : total,
           "Average marks": avg,
           "Grade": grade}
print(my_dict)