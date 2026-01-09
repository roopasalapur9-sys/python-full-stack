Employee_name=input("Enter employe name:")
salary=float(input("Enter salary:"))
performance_rating=int(input("performance-rating(1-5):"))
if performance_rating==5:
     bonus_rating=0.20
elif performance_rating==4:
     bonus_rating=0.15
elif performance_rating==3:
     bonus_rating=0.10
else:
     bonus_rating=0
bonus_amount=salary*bonus_rating
finale_salary=salary+bonus_amount
print("Employee_name:",Employee_name)
print("performance_rating:",performance_rating)
print("bonus_amount:",bonus_amount)
print("finale_salary:",finale_salary)
