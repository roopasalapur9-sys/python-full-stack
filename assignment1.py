intername=input("enter name:")
age=int(input("enter age:"))
email=input("enter email:")
contact=input("enter contact:")
grad=float(input("enter grade:"))
if age>=18:
    if grad>=60:
        if len(contact)==10:
           print("inter eligible for internship")
        else:
           print("contact number must be 10 digit")
    else:
        print("grade must be grater than 60")
else:
    print("age must be grater than 18")
        
