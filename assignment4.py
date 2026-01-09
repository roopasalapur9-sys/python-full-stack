course={
    "python programming":5000,
    "DataAnalysis":8000,
    "Ai&ml":12000
    }
course_name=input("enter course:")
is_student_discount=input("are you student (yes/no):")
is_early_registration=input("are you registred early(yes/no):")
if course_name not in course:
    print("course not found")
else:
    original_fees=course[course_name]
    discount=0

    if is_student_discount=="yes":
        discount+=0.10
    if is_early_registration=="yes":
        discount+=0.05
    total_discount=original_fees*discount
    final_fees=original_fees-total_discount
print("course name:",course_name)
print("original fees:",original_fees)
print("total discount:",total_discount)
print("final payable amount:",final_fees)
