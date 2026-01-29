import random
Name=input("Enter Your Full Name :")
Age=int(input("Enter Your  Age :"))
City=input("Enter  Your City :")
Skill=input("Enter Your Primary Skill :")
skill_level=input("Enter Your Skill Level :")
Choiceforskill_level=["BEGINNER","INTERMEDIATE","ADVANCE"]
if(Name=="" or Age<10 or Age>60 or Skill in Choiceforskill_level==0) :
    print("Error!! Program Stop")
else : 
    if(Age<18) : Career_Stage="Student"
    elif(Age>=18 or Age<=25) : Career_Stage="Early Professional"
    else : Career_Stage="Experienced Professional"
    if(Skill=="BEGINNER") : 
        Readliness_tag = "Foundation stage"
        Recommendation = "Focus on core fundamentals and consistency "
    elif(Skill=="INTERMEDIATE") : 
        Readliness_tag="Intern / Junior Ready"
        Recommendation = "Start building real-world projects"
    else : 
        Readliness_tag= "Production Ready"
        Recommendation ="Contribute to production-grade systems" 
print("*"*40)
print("             CANDIDATE PROFILE")
print("*"*40)
print(f"Name            : {Name.title()}")
print(f"Age             : {Age}")
print(f"City            : {City.title()}")
print(f"Skill           : {Skill.title()}")
print(f"Skill Level     : {skill_level}")
print(f"Readliness tag  : {Readliness_tag}")
print(f"Recommendation  : {Recommendation}")