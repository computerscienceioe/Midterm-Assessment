#==============================================================================#
#                             Shiven Viddemari                                 #
#                          October Midterm Assessment                          #  
#                               Due 28/10/20                                   #
#                            Status: Finished                                  #
#==============================================================================#





from time import sleep                                # For sleep timers
from os import system, name                           # For clearing console
from datetime import datetime                         # For Time references





#==============================================================================#


def goto(linenum):                # "goto" used for creating a menu in python
    global line                   # navigation is done by classifying codes by "lines" 
    line = linenum                # at the end of a code, it is redirected to menu (line 1)



"""                            _
LINE ONE: MENU                  |
LINE TWO: QUESTION 1            |             
LINE THREE: QUESTION 2          |               
LINE FOUR: QUESTION 3           |>   CONTENTS    
LINE FIVE: QUESTION 4           |               
LINE SIX: QUESTION 5            |
LINE SEVEN: QUESTION 6          |
LINE ZERO: EXIT                _|
"""




def clear():                                  
    if name == 'nt':                                 
        _ = system('cls')      
    else:                          
        _ = system('clear')      

present = datetime.now()       # datetime module makes life 100x easier, especially in Q1



class color:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'      # use at end of each line to stop color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# print(bcolors.UNDERLINE + "Warning: No active frommets remain. Continue?" + bcolors.WHITE)  



#==============================================================================#







#==============================================================================#
#                                   MENU                                       #
#==============================================================================#

line = 1
while True:
    if line == 1:
        print("")
        print("")
        sleep(1)
        print(color.RED + "Redirecting" + color.WHITE)
        sleep(5)
        clear()
        print("")
        print("")
        print(color.RED + "Refreshing Console, Please wait (4)")
        sleep(1)
        clear()
        print("")
        print("")
        print(color.RED + "Refreshing Console, Please wait (3)")
        sleep(1)
        clear()
        print("")
        print("")
        print(color.RED + "Refreshing Console, Please wait (2)")
        sleep(1)
        clear()
        print("")
        print("")
        print(color.RED + "Refreshing Console, Please wait (1)")
        sleep(1)
        clear()
        response = input(color.GREEN + "Hello! Welcome to my October Midterm Assessment\nWhich question do you want to go to? 1, 2, 3, 4, 5, or 6?\nTo exit, enter 0: " + color.WHITE)


        if response == "1":
           sleep(2)
           clear()
           goto(2)


        elif response == "2":
            sleep(2)
            clear()
            goto(3)

        elif response == "3":
           sleep(2)
           clear()
           goto(4)

        elif response == "4":
           sleep(2)
           clear()
           goto(5)

        elif response == "5":
           sleep(2)
           clear()
           goto(6)

        elif response == "6":
           sleep(2)
           clear()
           goto(7)
        
        elif response == "0":
           sleep(2)
           print("Cya!")
           exit()
          
          

        else:
            goto(100)









#==============================================================================#
#                             Question 1    (Completed)                        #
#==============================================================================#


    elif line == 2:
        print("")
        print("")
        print("")
        print(color.UNDERLINE + "Question One: Birthday Calculator" + color.WHITE)
        print("")
        print("")
        print("")
        sleep(2)
        clear()
        #codestart

             
        # Asking user for name   
        name = input("Hey! What's your name? " + color.CYAN)
        sleep(0.5)
        print("")

        # Asking user for Date Of Birth
        birthdayin = str(input( color.WHITE +

          "Please enter your date of birth in the form DD/MM/YY: "
          
          ))

        sleep(0.5)  
        print("")



        # Changing input into %d/%m/%y format
        birthday = datetime.strptime(birthdayin, '%d/%m/%Y')
        check = input("Did you pass your birthday this year? Enter y for Yes or n for No: ")
        



        # Sleep timers to simulate slower calculation
        sleep(1)
        print("Caclulating...")
        sleep(2)



        # Calculating birthday through datetime module
        countdown = present - birthday
        age = int(countdown.days/365.25)       



        # Final Answers      
        print(name,"You are", age,"years old!" )




       #codeend


        goto(1)












#==============================================================================#
#                             Question 2      (Completed)                      #
#==============================================================================#




    elif line == 3:
        print("")
        print("")
        print("")
        print("Question Two: Leap Year Check")
        print("")
        print("")
        print("")
        sleep(2)
        clear()


      #codestart
       
        def leapyear():
           year = int(input("Please enter a year to check if it is a leap year or not: "))


           if year % 4 > 0:
              print("The year you entered,", year, " is not a leap year")

           elif year % 100 == 0 and year % 400 != 0:     # Unless the year is divisible by 100, then it is not a leap year  
             sleep(1)                                    # Unless the year is divisible by 400, then it is a leap year
             print("The year you entered,", year, " is not a leap year")

           elif year % 4 == 0:                             #  # If a year is divisible by 4 it is a leap year
             sleep(1)
             print("The year you entered,", year, " was a leap year")          # output




       
        leapyear()      
      #codeend


        goto(1)
    










#==============================================================================#
#                             Question 3      (Completed)                      #
#==============================================================================#



    elif line == 4:
       


       #codestart
        print("")
        print("")
        print("")
        print("Question Three: Number Steps")
        print("")
        print("")
        print("")
        sleep(2)
        clear()
       
        def numstep():
            num_in = int(input("Please enter your starting number: "))    # Asking user for Starting number
            sleep(1)
            print("")
            num_end = int(input("Please enter your ending number: "))   # Asking user for Ending number
            print("")
            sleep(1)
            num_step = int(input("Enter your step number here: "))     # Asking user for interval number
            print("")
            sleep(1)
            print("The result is....")
            print("")
            sleep(1)
            for i in range (num_in, num_end, num_step):
               print(i)
        
        numstep()
       #codeend


        goto(1)






#==============================================================================#
#                             Question 4    (Completed)                        #
#==============================================================================#


    elif line == 5:

      #codestart
       print("")
       print("")
       print("")
       print("Question Four: Grades")
       print("")
       print("")
       print("")
       sleep(2)
       clear()
       grades = []


       grade_num = int(input("Enter the number of grades you wish to input: ")) # User input for grades

       for i in range(grade_num):
          grades.append(int(input("Grade: ")))
        
       print()
        
       sum = 0
       for i in range(len(grades)):
          sum += grades[i]

       print("The average grade is", sum/len(grades))

       lowestGrade = 100                  # Set it to the highest grade possible at the start. 
       for i in range(len(grades)):
          if grades[i] < lowestGrade:
            lowestGrade = grades[i]

       print("The lowest grade is", lowestGrade)

       grade_max = 0                   # Set it to the lowest grade possible at the start. 
       for i in range(len(grades)):
          if grades[i] > grade_max:
            grade_max = grades[i]

       print("The highest grade is", grade_max)  

       goto(1)
       



       
#==============================================================================#
#                             Question 5      (Completed)                      #
#==============================================================================#


    elif line == 6:

      #codestart
       print("")
       print("")
       print("")
       print("Question Five: Grades Increased by 25%")
       print("")
       print("")
       print("")
       sleep(2)
       clear()


       grades = []


       numGrades = int(input("Enter the number of grades you wish to input: "))

       for i in range(numGrades):
         grades.append(int(input("Grade: ")))

       for i in range(len(grades)):
         grades[i] *= 1.25
         
       for i in range(len(grades)):
         if grades[i] > 100:
           grades[i] = 100

       print("The new grades are:",grades)


       goto(1)




#==============================================================================#
#                             Question 6      (Completed)                      #
#==============================================================================#


    elif line == 7:

      #codestart
       print("")
       print("")
       print("")
       print("Question Six: Students' Marks")
       print("")
       print("")
       print("")
       sleep(2)
       clear()

       numStudents = int(input("How many students would you like to enter? "))
       totalPossibleMarks = int(input("How much is the maximum amount of marks on the test "))

       names = []
       marks = []

       for i in range(numStudents):
         names.append(input("Enter the name of the student: "))    # Asks user for name of the student
         mark = int(input("Enter the mark this person got: "))    # Asks user for the grade the student got
         while mark > totalPossibleMarks:
           print("Invalid entry")
           mark = int(input("Enter the mark: "))
         marks.append(mark)
  
       per = []
       for i in range(len(marks)):
         per.append((marks[i]/totalPossibleMarks)*100)
  
       grades = []
       for i in range(len(per)):
         if per[i] >= 90 and per[i] <= 100:
           grades.append("H1")
         elif per[i] >= 80 and per[i] < 90:
           grades.append("H2")
         elif per[i] >= 70 and per[i] < 80:
           grades.append("H3")
         elif per[i] >= 60 and per[i] < 70:               # } Allocating the marks to grades  
           grades.append("H4")
         elif per[i] >= 50 and per[i] < 60:
           grades.append("H5")  
         elif per[i] >= 40 and per[i] < 50:
           grades.append("H6")
         elif per[i] >= 30 and per[i] < 40:
           grades.append("H7")
         elif per[i] >= 0 and per[i] < 30:
           grades.append("H8")

       print("")
       print("")
       print("")       

       print("Name\tper\tGrade")
       for i in range(len(marks)):
         print(names[i], "\t", per[i], "\t\t", grades[i], sep="")




       goto(1)



#==============================================================================#



    elif line == 20:
        break


#==============================================================================#
#                            Invalid Response                                  #
#==============================================================================#

    elif line == 100:
        print("Please enter a valid question")              # Sends user back to menu if an invalid response is given
        goto(1)
































