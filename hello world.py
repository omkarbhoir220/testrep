s1=(input("Enter the student 1 marks:"))
s2=(input("Enter the student 2 marks:"))
s3=(input("Enter the student 3 marks:"))
s4=(input("Enter the student 4 marks:"))

if(s1>s4):
    f1=s1
else:
    f1=s4

if(s2>s3):
    f2=s2
else:
    f2=s3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")
