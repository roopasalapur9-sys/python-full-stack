distance=int(input("Enter delivery distance in km:"))
if distance <=5:
    print("Local Delivery")
elif distance>=6 and distance<=20:
    print("City Delivery")
else:
    print("Outstation Delivery")
