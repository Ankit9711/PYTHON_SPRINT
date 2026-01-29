
Name=input("Enter patient name: ").strip().title()
Age=int(input("Enter age: "))
Heart_ratecount=int(input("Enter number of heart readings: "))
Warning=[]
Flag=[]
Status=""

def heart(Heart_ratecount) :
    if(Heart_ratecount==0) : return
    else : 
        H=int(input("Enter  heart readings: "))
        if(H>180) : Warning.append("High Heart Rate Detected")
        if(type(H)!=int) : Flag.append("Invalid Heart Rate")
        heart(Heart_ratecount-1)

def AGE(Age) :
    if(Age>=0 and Age<=120) : 
        return
    else :
        Flag.append("Invalid Age")
        return

heart(Heart_ratecount)
AGE(Age)
if(len(Flag)!=0) : Status="Fail"
elif(len(Flag)==0 and len(Warning)!=0) : Status="Review"
else : Status="Pass"

if(Status=="Pass") : 
    Flag.clear()
    Warning=None
elif(Status=="Fail") : Warning=None
else : Flag=None

print(f"Patient : {Name}")
print(f"Staus   : {Status}")
print(f"Flag    : {Flag}")
print(f"Warning : {Warning}")
