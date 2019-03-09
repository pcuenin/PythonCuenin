st=int(input("How many students do you have?")) 
for x in range(1,st+1):             #run loop for each student starting with 1
    print("")
    print("********************")
    print("Taking input for Student #",x)
    nm=str(input("What is your name? "))
    cls=int(input("How many classes are you taking? "))
    print("")
    tq=0    #set total quality points to 0
    tc=0    #set total credits hours to 0
    for y in range(1,cls+1):        #run grade loop for each class starting with 1
        print("Data for Class #",y)
        gr=int(input("What is your numerical grade? "))
        cr=int(input("How many credit hours is it for? "))
        if gr>=90:      #set point value based on numerical grade
            pv=4                    #pv is short for point value
        elif gr>=80:
            pv=3
        elif gr>=70:
            pv=2
        elif gr>=60:
            pv=1
        else:
            pv=0
        qp=pv*cr    #get quality points by multiplying point value and credit hours
        tq+=qp      #sum total quality points
        tc+=cr      #sum total credit hours
        print("")
    gpa=tq/tc       #find GPA by dividing total quality points by total credit hours
    print(nm," your GPA is ",gpa) 
    if gpa==4:      #set message based on gpa
        print("You are on the Presidents list! :-)")
    elif gpa>=3.5:
        print("You are on the Deans list!")
    elif gpa>=2.0:
        print("You are doing Okay, but work hard to improve your grade.")
    else:
        print("You will be on probation for the next semester. :-(")
    
    
