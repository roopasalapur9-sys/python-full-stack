intername=input("enter employee name:")
employee_ID=int(input("enter employee_ID:"))
basic_salary=float(input("basic_salary:"))
HRA=0.20*basic_salary
DA=0.10*basic_salary
PF=0.12*basic_salary
net_salary=basic_salary+HRA+DA-PF
print("net_salary is:",net_salary)
print("HRA is:",HRA)
print("DA is:",DA)
print("PF is:",PF)
                
