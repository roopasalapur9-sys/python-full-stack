student={"Ashs":"python","Ravi":"data analytics","Neha":"AI"}
print("student name:")
for name in student:
    print(name)
print("courses:")
for courses in student:
    print(courses)
search=input("enter student name to check:")
if search in student:
    print("student exists")
else:
    print("student not found")
