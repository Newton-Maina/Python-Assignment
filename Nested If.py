maths = int(input("Enter Your Math score: "))
physics = int(input("Enter your Physics score: "))
geo = int(input("Enter your Geography score: "))
chem = int(input("Enter your Chemistry score: "))

avg = (maths + physics + geo + chem)/4

if avg >=71 and avg <=100:
    print("Your Grade is A")
elif avg >=51 and avg <=70:
    print("Your Grade is B")
elif avg >=31 and avg <=50:
    print("Your Grade is C")
elif avg >=0 and avg <=30:
    print("Your Grade is D")
else:
    print("Unrecognized marks/avg")