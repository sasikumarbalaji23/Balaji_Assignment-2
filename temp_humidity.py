import random 
while(True):
    a=random.randint(10,99) 
    b=random.randint(10,99) 
    if(a>35 and b>60):
        print("High Temperature and Humidity of:",a,b,"%","Alarm is ON") 
    elif(a<35 and b<60):
        print("Normal Temperature and Humidity of:",a,b,"%","Alarm is OFF") 
    break
