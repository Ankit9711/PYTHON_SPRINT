Name=input("Enter Your Full Name:").title()
Roll_no=int(input("Enter Roll No.:"))
Branch=input("Enter Branch:").upper()
FAV_sub1,FAV_sub2,FAV_sub3=map(str,input("Enter 3 Favourite Subjects(Comma Separated):").split(','))
FavouriteSubject=[]
Mark1=int(input(f"Enter Marks of {FAV_sub1.upper()}:"))
Mark2=int(input(f"Enter Marks of {FAV_sub2.upper()}:"))
Mark3=int(input(f"Enter Marks of {FAV_sub3.upper()}:"))
Techskill_1,Techskill_2,Techskill_3=map(str,input("Enter Your ANY THREE TechSkills(Comma Separated):").split(','))
FavouriteSubject.append(FAV_sub1.upper())
FavouriteSubject.append(FAV_sub2.upper())
FavouriteSubject.append(FAV_sub3.upper())
FavouriteSubject.sort()
t=()
l=list(t)
l.append(Roll_no)
l.append(Branch)
i=tuple(l)
Marks={FAV_sub1.upper(): Mark1,FAV_sub2.upper(): Mark2,FAV_sub3.upper(): Mark3}
def max(a,b,c) :
    if(a>=b and a>=c) : return a
    elif(b>=a and b>=c) : return b
    else : return c
S=set()
S.add(Techskill_1.title())
S.add(Techskill_2.title())
S.add(Techskill_3.title())
TOTALMARK=Mark1+Mark2+Mark3
AVG_MARK=TOTALMARK/3
HIGHSCORE=max(Mark1,Mark2,Mark3)
HIGHSCORE_SUBJECT=""
for i,j in Marks.items() :
    if(j == HIGHSCORE) :
        HIGHSCORE_SUBJECT+=i
print("-"*7,end="")
print("STUDENT DETAIL",end="")
print("-"*10)
print(f"NAME               :{Name}")
print(f"ROLLNO. & BRANCH   :{Roll_no}, {Branch}")
print(f"FAVORITE SUBJECTS  :{FavouriteSubject}")
print(f"SUBJECT WITH MARKS :{Marks}")
print(f"TOTAL MARKS        :{TOTALMARK}")
print(f"AVERAGE MARKS      :{AVG_MARK}")
print(f"HIGHSCORINGSUBJECT :{HIGHSCORE_SUBJECT}")
print(f"TECHNICAL SKILLS   :{S}")
