def calcAverage(score1, score2, score3, score4, score5):
   average = (score1 + score2 + score3 + score4 + score5) / 5
   return average

def determineGrade( userScore ):
       if( userScore < 60 ):
           return "F"
       elif( userScore < 70 ):
           return "D"
       elif( userScore < 80 ):
            return "C"
       elif( userScore < 90 ):
           return "B"            
       elif( userScore < 101 ):
           return "A"

def askforScores():
   score1 = float( input( "Please enter score 1: " ) )
   score2 = float( input( "Please enter score 2: " ) )
   score3 = float( input( "Please enter score 3: " ) )
   score4 = float( input( "Please enter score 4: " ) )
   score5 = float( input( "Please enter score 5: " ) )

   return score1, score2, score3, score4, score5

def printTableOfResults( score1, score2, score3, score4, score5 ):
    print( "Score\tletter Grade" )
    print( str( score1 ) + "\t" + determineGrade( score1 ),
           str( score2 ) + "\t" + determineGrade( score2 ), 
           str( score3 ) + "\t" + determineGrade( score3 ), 
           str( score4 ) + "\t" + determineGrade( score4 ), 
           str( score5 ) + "\t" + determineGrade( score5 ), sep= "\n" ) 

def main():
     score1, score2, score3, score4, score5 = askforScores()
     printTableOfResults( score1, score2, score3, score4, score5 )

main()

