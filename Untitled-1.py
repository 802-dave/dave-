

Applicant_name = input('Name: ')
Gender = input ('Gender: ')
if Gender != 'M' and Gender != 'Male' and Gender != 'F' and Gender != 'Female':
    print("""
    Please select Gender. Insert as 'M' or 'Male' for Male,
    'F' or 'Female' for female.
    """)
    Gender = input("Gender: ")

Course_name = input('Course: ')
if Course_name != 'Engineering' and Course_name != 'Medicine' and Course_name != 'Law' and Course_name != 'Economics':
    print("""
    Please enter Course. Insert as 'Engineering' or 'Medicine' for Sciences,
    'Law' or 'Economics' for Arts.
    """)
    Course_name = input('Course: ')

Introduction = print(f'''
\n
Hi {Applicant_name}, thank you for deciding to apply for a(n) {Course_name} course, at Kyambogo University.
Please fill in the relevant information required below;''')



gradedictionary = {"A" : "6" ,
                   "B" : "5" ,
                   "C" : "4",
                   "D" : "3",
                   "E" : "2",
                   "O" : "1",
                   "F" : "0",
                  } 
marks = input('Respective points for principles in uppercase: ').split()
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

grading = {"A":6, "B":5, "C":4, "D":3, "E":2, "O":1, "F":0}
output = ''

for ch in marks:
    output+=str(grading.get(ch))

a = output[0]
b = output[1]
c = output[2]

a = int(a)
b = int(b)
c = int(c)


total_points = a + b + c + GEP_point + sub_grade + Gender_point
total_points = float(total_points)

for_weights = [a, b, c]
for_weights.sort(reverse=True)
top_two_for_weights = (for_weights[0] + for_weights[1])*3
last_for_weights = (for_weights[2])*2 + GEP_point + sub_grade

total_weights_main = top_two_for_weights + last_for_weights
total_weights_main = float(total_weights_main)

print('\n')
print('\n')
print(f'''{Applicant_name}
Results:
''')

print(str(principles[0]) + ': '+ str(marks[0]))
print(str(principles[1]) + ': '+ str(marks[1]))
print(str(principles[2]) + ': '+ str(marks[2]))
print(Subsidiary_subjects +': '+ str(sub_grade))
print('GEP:' + str(GEP))
print('\ntotal_points: ' + str(total_points))
print('weights: ' + str(total_weights_main))

