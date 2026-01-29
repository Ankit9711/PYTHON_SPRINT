exp=int(input("Enter No. of Expenses:"))
L_Exp=[]
d_CategwithExp={}
status=""
for i in range(1,exp+1) :
    Exp_am=int(input(f"Expenses{i} Amount  : "))
    if(Exp_am>500) : status="High Expense Detected"
    Exp_categ=input(f"Expenses{i} Category: ").upper()
    print("\n\n")
    d_CategwithExp[Exp_categ]=d_CategwithExp.get(Exp_categ,0)+Exp_am
print(f"{status}\n")
for i in d_CategwithExp.values() :
    L_Exp.append(i)
Total=0
for item  in L_Exp :
    Total+=item
print(f"Total Expense  ={Total}")
Avgexp=Total/exp
print(f"Average Expense={round(Avgexp)}")
print("\n\n")
print("Category_Wise Expenses:")
max=[]
L_Exp.sort()
min=L_Exp[-1]
for i,j in d_CategwithExp.items() :
    print(f"{i} : {j}")
    if(j==min)  :  max.append(i) 
print("\n\n")
print(f"Highest Spending Category:{max}")
print(f"Spending Status: ",end="")
if(Avgexp<=200)   : print("Controlled Spending")
elif(Avgexp<=400) : print("Moderate Spending")
else              : print("High Spending")