Map("A" == 6, "B"== 5, "C"== 4, "D"== 3, "E"== 2, "O"== 2, "F"== 0)

 if best == "A"
    weight == Map("A" * 3)
	    
	   
		 

def PrintExplanation():
		 {
		     #("This program will calculate your semester GPA for one semester." + "\n" +
			 # "You will be asked to enter the name, credits, and grade in each course that " +
			 #"was taken using the regular grading method." + "\n" + "Please do NOT enter Pass/Fail");
		 }


		 def GetValidNumberInput(promptString, lowerNum, upper()
		 {
		 do
		 {
 		var value;
			value = prompt(promptString);
			value = parseInt(value);

		   while(value < 0 || value > 4)
			{
			  #("You must enter a value between 1 and 4.");
			  value = prompt(promptString);
			  value = parseInt(value);
			}
		   return value;
		 }while (value != "end")  
		 } 

		 function GenerateGradeReport(semester, totalCredits, totalPoints)
		 {
		   CalculateGPA(totalCredits, totalPoints);
			  document.write("<h1>GPA report for " + semester + ".</h1>" + "<br />");
		   document.write("<p>Credits taken: " + totalCredits+ ".</p>");
		   document.write("<p>Quality points earned: " + totalPoints + ".</p>");
		   document.write("<p>GPA for " + semester + "is " + GPA.toFixed(3) + ".</p>");
		 }

	   
def ConvertGradeToPoints(grade)
		 { 
		 do
		 {
		   grade = prompt("Enter grade received for the course: ");
		   
		   if (grade 
		   if (grade == "B")points=5;
		   if (grade == "C")points=4;
		   if (grade == "D")points=3;
		   if (grade == "E")points=2;
		   if (grade == "O")points=1;
		   if (grade == "F")points=0;
		   
		   document.write("Grade Earned: " + grade + " " + " ");
		   totalPoints = (points + totalPoints);			  
		 }while (grade != "end")   
		 }  
		 
		 function GenerateGradeReport(semester, totalCredits, totalPoints)
		 {
		   CalculateGPA(totalCredits, totalPoints)
	   document.write("<h1>GPA Report For " + semester + "</h1>" + "<br /><br />");
		   document.write("<p>Total credits taken: " + totalCredits + "</p>");
		   document.write("Total quality points earned: " + totalPoints + "</p>");
		   document.write("Your GPA for " + semester + ": " + GPA.toFixed(3) + "</p>");
		 }
				
		 function CalculateGPA(totalCredits, totalPoints)
		 {
		   GPA =  (totalPoints / totalCredits);
		   return GPA;
		 }
   


  
   
	   <script type="text/javascript">
	   <!--
		 var semester;
		 var credits = 0;
		 var points = 0;
		 var totalCredits = 0;
		 var totalPoints = 0;
		 var gpa = 0;
		 var grade = 0;
		 var letterGrade;
		 var value;
		 var courseName;


		 PrintExplanation();
		 
	  semester = prompt("Enter the semester:");
		 document.write("<h1>" + semester + "</h1>")
		 
		 do
		 {
		 courseName = prompt("Enter name of course:")
		 document.write(courseName + " " + " ")
	  
		 credits = GetValidNumberInput("Enter the number of possible credits for the course");
		 document.write("Possible credits: " + credits)
   
		 function ConvertGradeToPoints(grade)
		 totalPoints = (totalPoints + points)
		 document.write(credits + " " + totalCredits)
		 }while(courseName != "end")
	   
 

		 GenerateGradeReport(semester, totalCredits, totalPoints);
		   

	



