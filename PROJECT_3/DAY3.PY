User=input("Enter Name: ").title()
print("AVALIABLE PRODUCTS :")
print("1. LAPTOP   : $4500(ELECTRONICS)")
print("2. MOBILE   : $2500(ELECTRONICS)")
print("3. SHIRT    : $180(CLOTHING)") 
print("4. HORLICKS : $45(GROCERY)")
P1,P2,P3=map(int,input("Select any 3 Product(1-4:").split(','))
def name(x) :
    Product=""
    if(x==1) : 
        Product+="LAPTOP"
        return Product
    elif(x==2) : 
        Product+="MOBILE"
        return Product
    elif(x==3) : 
        Product+="SHIRT"
        return Product
    else : 
        Product+="HORLICKS"
        return Product
def cost(x) :
    price=0
    if(x==1) : 
        price+=4500
        return price
    elif(x==2) : 
        price+=2500
        return price
    elif(x==3) : 
        price+=180
        return price
    else : 
        price+=45
        return price
def type(x) :
    category=""
    if(x==1 or x==2) : 
        category+="ELECTRONICS"
        return category
    elif(x==3) : 
        category+="CLOTHING"
        return category
    else : 
        category+="GROCERY"
        return category
product1=name(P1)
product2=name(P2)
product3=name(P3)
price1=cost(P1)
price2=cost(P2)
price3=cost(P3)
PRODUCTS=[product1,product2,product3]
Productwithcost={product1:price1,product2:price2,product3:price3}
category1=type(P1)
category2=type(P2)
category3=type(P3)
s={category1,category2,category3}
payment=input("ENTER PAYMENT METHOD(UPI/CARD/COD): ")
Totalcart = price1+price2+price3
Discountpercent=0
if(Totalcart>500) : Discountpercent=20
elif(Totalcart>200) : Discountpercent=10
else : Discountpercent=0
Status="ORDER SUCESSFULL"
if("ELECTRONICS" in s and payment=="COD" ) : 
    Status="Order Not Allowed(ELECTRONICS+COD)"
if(payment=="CARD" and Totalcart>3000 ) : Discountpercent=5
FINALPRICE=Totalcart-(Totalcart*Discountpercent/100)
print("="*35)
print("     PURCHASE SUMMARY")
print("="*35)
print(f"USER            : {User}")
print(f"Products        : {PRODUCTS}")
print(f"Categories      : {s}")
print(f"Payment         : {payment}\n") 
print(f"Cart Total      : {Totalcart}$")
print(f"Discountpercent : {Discountpercent}%")
print(f"Final Price     : {FINALPRICE}$")
print(f"Status          : {Status}")
print("="*35)

  