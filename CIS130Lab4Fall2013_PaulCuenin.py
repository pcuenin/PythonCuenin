# Write a program to determine the GPA of a student. The student is taking three classes.
# GPA is calculated by dividing the total quality points obtained by the total credit hours
# earned. The quality points for a course are obtained by multiplying the number of credits
# earned for that class by a point value determined by the student’s numeric grade.
g1=int(input("What was your percent grade for your first class?"))
g2=int(input("What was your percent grade for your second class?"))
g3=int(input("What was your percent grade for your third class?"))
h1=int(input("How many hours was your first class?"))
h2=int(input("How many hours was your second class?"))
h3=int(input("How many hours was your third class?"))
if g1>=90:
    g1=4
elif g1>=80:
    g1=3
elif g1>=70:
    g1=2
elif g1>=60:
    g1=1
else:
    g1=0
if g2>=90:
    g2=4
elif g2>=80:
    g2=3
elif g2>=70:
    g2=2
elif g2>=60:
    g2=1
else:
    g2=0
if g3>=90:
    g3=4
elif g3>=80:
    g3=3
elif g3>=70:
    g3=2
elif g3>=60:
    g3=1
else:
    g3=0
sq=g1*h1+g2*h2+g3*h3
sh=h1+h2+h3
gpa=sq/sh
print("Your Total Credit Hours earned is ",sh," and your GPA is ",gpa)

    
