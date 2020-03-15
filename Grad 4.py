
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



gradedictionary = {"A" : "6" ,
                   "B" : "5" ,
                   "C" : "4",
                   "D" : "3",
                   "E" : "2",
                   "O" : "1",
                   "F" : "0",
                  } 
Subsidiary_subjects = input("Enter your subsidiary subject: ")
sub_grade = input("Sub-aggregate: ")
GEP = input("GEP marks: ")

GEP = int(GEP)
sub_grade = int(sub_grade)

GEP_point = 0
sub_grade = 0
Gender_point = 0

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
       
principles = input("Enter essential subject 1: ")
principles = input("Enter essential subject 2: ")
principles = input("Enter relevant subject: ")

def askforGrade():
   grade1 = str( input( "Please enter essential grade 1: " ) )
   grade2 = str( input( "Please enter essential grade 2: " ) )
   grade3 = str( input( "Please enter relevant subject: " ) )


   return grade1, grade2, grade3
  
def printTableOfResults( grade1, grade2, grade3 ):
    print( "Score\tnumber Grade" )
    print( str( grade1 ) + "\t" + gradedictionary[ grade1 ],
           str( grade2 ) + "\t" + gradedictionary[ grade2 ], 
           str( grade3 ) + "\t" + gradedictionary[ grade3 ],  sep= "\n" ) 
  
def main():
     score1, score2, score3 = askforGrade()
     printTableOfResults( score1, score2, score3 )


main()

score1 = output[0]
score2 = output[1]
score3 = output[2]

score1 = int(score1)
score2 = int(score2)
score3 = int(score3)


total_points = score1 + score2 + score3 + GEP_point + sub_grade + Gender_point
total_points = float(total_points)


   
