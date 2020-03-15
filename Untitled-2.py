
Applicant_name = input('Name: ')
Gender = input ('Gender: ')
if Gender != 'M' and Gender != 'Male' and Gender != 'F' and Gender != 'Female':
    print("""
    Please select Gender. Insert as 'M' or 'Male' for Male,
    'F' or 'Female' for female.
    """)
    Gender = input("Gender: ")

Course_name = input('Course: ')

Introduction = print(f'''
\n
Hello {Applicant_name}, thank you for deciding to apply for an {Course_name} course, at Kyambogo University.
Please fill in the relevant information required below;''')

subject = input("For subjects, please insert a space between said subjects.\nAll three principle subjects: ").split()
marks = input('Enter received marks in Uppercase letters: ').split()
Subsidiary_subjects = input("Enter your subsidiary subject: ")
sub_grade = input("Sub-aggregate: ")
GEP = input("GEP marks: ")

GEP = int(GEP)
sub_grade = int(sub_grade)

GEP_point = 0
sub_grade = 0
gendeer_point = 0

if Gender == 'F' or Gender == 'Female':
    Gender_point = 1.5
else:
    pass

if sub_grade > 0  and sub_grade <= 6:
    sub_point = 1
elif sub_grade > 6:
    pass

if GEP > 50 and GEP <= 100:
    GEP_point = 1
elif GEP < 50:
    pass