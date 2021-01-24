def q1():
  # 2 marks
  print("This will calculate your age: ")
  name = input("Enter your name: ")
  yearOfBirth = int(input("Enter your year of birth: "))
  
  # 2 marks
  birthdayThisYear = input("Have you had a birthday yet this year? y or n?")

  # 4 marks
  if birthdayThisYear == 'y':
    age = 2020-yearOfBirth
  else:
    age = 2020-yearOfBirth-1

  # 2 marks
  print("Hi", name, ", you are", age, "years old.")



def q2():
  # 2 marks
  year = int(input("Enter a year?"))
  # 8 marks
  if year % 400 == 0:
    print("The year", year, "is a leap year")
  elif year % 100 == 0:
    print("The year", year, "is not a leap year")
  elif year % 4 == 0:
    print("The year", year, "is a leap year")
  else:
    print("The year", year, "is not a leap year")

def q3():
  # 4 marks
  startNum = int(input("Enter the first number: "))
  lastNum = int(input("Enter the last number: "))
  step = int(input("Enter the step size"))

  # 6 marks
  for i in range(startNum,lastNum, step):
    print(i)

def q4():
  # 2 marks
  amount = int(input("How many grades would you like to enter? "))
  # 4 marks
  numbers = []
  for i in range(amount):
    numbers.append(float(input("Enter number: ")))
  # 4 marks
  sum = 0;
  for i in range(len(numbers)):
    sum += numbers[i]
  # print(sum)
  print("The average grade is", sum/len(numbers))

  # 5 marks
  max = 0
  min = 100
  for i in range(len(numbers)):
    if numbers[i] > max:
      max = numbers[i]
    if numbers[i] < min:
      min = numbers[i]
  print("The Lowest Grade is", min)
  print("The highest Grade is", max)

def q5():
  # 2 marks
  amount = int(input("How many grades would you like to enter? "))
  # 4 marks
  numbers = []
  for i in range(amount):
    numbers.append(float(input("Enter number: ")))
  # 5 marks
  for i in range(len(numbers)):
    numbers[i] *= 1.25
  # 4 marks
  for i in range(len(numbers)):
    if numbers[i] > 100:
      numbers[i] = 100
  print(numbers)

def q6():
  # 2 marks
  numStudents = int(input("How many students would you like to enter? "))
  totalPossibleMarks = int(input("How many marks can you get on the test? "))
  # 2 marks
  names = []
  marks = []
  for i in range(numStudents):
    names.append(input("Enter the name: "))
    mark = int(input("Enter the mark: "))
    # 4 marks
    while mark > totalPossibleMarks:
      print("Invalid entry")
      mark = int(input("Enter the mark: "))
    marks.append(mark)
  
  # 2 marks
  percentages = []
  for i in range(len(marks)):
    percentages.append((marks[i]/totalPossibleMarks)*100)
  
  # 3 marks
  grades = []
  for i in range(len(percentages)):
    if percentages[i] > 90 and percentages[i] <= 100:
      grades.append("H1")
    elif percentages[i] > 80 and percentages[i] <= 90:
      grades.append("H2")
    elif percentages[i] > 70 and percentages[i] <= 80:
      grades.append("H3")
    elif percentages[i] > 60 and percentages[i] <= 70:
      grades.append("H4")
    elif percentages[i] > 50 and percentages[i] <= 60:
      grades.append("H5")
    elif percentages[i] > 40 and percentages[i] <= 50:
      grades.append("H6")
    elif percentages[i] > 30 and percentages[i] <= 40:
      grades.append("H7")
    elif percentages[i] > 00 and percentages[i] <= 30:
      grades.append("H8")

  # 2 marks - presentation
  # print(names)
  # print(percentage)
  # print(grades)

  print("TABLE OF RESULTS \n====================\n Name\t Grade \t Percentage \t Orignal Mark")
  for i in range(numStudents):
    print("--------------------")
    print("| " + names[i] + "\t|\t" + grades[i] + "\t|\t" + str(percentages[i]) + "\t|\t" + str(marks[i]))
  print("--------------------")
  
def menuInstructions():
  print("Here are your options. Enter the option number to start ")
  print()
  print(" 1. Age Calculator")
  print(" 2. Leap Year Detection")
  print(" 3. Counting with Steps")
  print(" 4. Average, Highest, and Lowest Grade Calculation")
  print(" 5. Grade Increment Calculation")
  print(" 6. Grade and Percentage Calculation")
  print()
  print(" Enter 0 to exit")
  print() 
# 2 marks
menuInstructions()
option = int(input("Choose an option: "))
# 2 marks
while option != 0:
  # 2 marks
  if option == 1:
    q1()
  elif option == 2:
    q2()
  elif option == 3:
    q3()
  elif option == 4:
    q4()
  elif option == 5:
    q5()
  elif option == 6:
    q6()
  # 2 marks
  else:
    print("Invalid entry")
  # 2 marks
  menuInstructions()
  option = int(input("Choose an option: "))

print("You are exiting the program")



# Presentation marks of 8
# 1 marks for basic menu
# 2 marks for more on the menu
# 2 marks for Q6
# 2 marks for all other questions
# 1 marks for something extra

# Neat, clear code marks of 7
# 3 marks for full names
# 4 marks for good clear names
