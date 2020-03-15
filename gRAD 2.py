def calcAverage(score1, score2, score3, score4, score5):
   average = (score1 + score2 + score3 + score4 + score5) / 5
   return average

gradedictionary = {"A" : "6" ,
                   "B" : "5" ,
                   "C" : "4",
                   "D" : "3",
                   "E" : "2",
                   "O" : "1",
                   "F" : "0",
                  }

def askforGrade():
   grade1 = str( input( "Please enter essential 1: " ) )
   grade2 = str( input( "Please enter essential 2: " ) )
   grade3 = str( input( "Please enter relevant 3: " ) )
   grade4 = str( input( "Please enter subcidiary 1: " ) )
   grade5 = str( input( "Please enter subcidiary 2: " ) )

   return grade1, grade2, grade3, grade4, grade5

def printTableOfResults( grade1, grade2, grade3, grade4, grade5 ):
    print( "Score\tnumber Grade" )
    print( str( grade1 ) + "\t" + gradedictionary[ grade1 * 3 ],
           str( grade2 ) + "\t" + gradedictionary[ grade2 ], 
           str( grade3 ) + "\t" + gradedictionary[ grade3 ], 
           str( grade4 ) + "\t" + gradedictionary[ grade4 ], 
           str( grade5 ) + "\t" + gradedictionary[ grade5 ], sep= "\n" ) 

def main():
     score1, score2, score3, score4, score5 = askforGrade()
     printTableOfResults( score1, score2, score3, score4, score5 )

main()

