################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")


# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

################ Main Program ################
studentDictionary = {}

# Application Loop
# Starting value to begin loop
userInput = "8"

# Continue loop until 6 is entered
while userInput != "6":
  
  # Prompt the user to select an option
  print()
  displayMenu()
  userAddedInput = input("Select an Option: ")
  userInput = userAddedInput

# Add student's name if 1 is inputted
  if userInput == "1":
    studentName = input("Enter student name to add: ")
    studentDictionary[studentName] = []
    print(f"{studentName} added!")
    
# Remove student's name if 2 is inputted   
  elif userInput == "2":
    removeName = input("Enter student name to remove: ")
# Removes student name if exist in dictionary
    if removeName in studentDictionary:
      studentDictionary.pop(removeName,None)
      print(f"{removeName} removed!")
# Gives error if name doesn't exist
    else:
      print(f"{removeName} is not in the dictionary")

# Add quiz grade if 3 is inputted
  elif userInput == "3":
# Search name
    gradeName = input("Enter a student name: ")
# Checks if name exists to add grade
    if gradeName in studentDictionary:
      grades = getNumberGradeFromUser()
      studentDictionary[gradeName].append(grades)
      print(f"Added {grades} to {gradeName}'s quizzes")
# Gives error if name doesn't exist
    else:
      print(f"{gradeName} is not in the dictionary")

# Lists grades
  elif userInput == "4":
    studentName4 = input("Enter a student name: ")
# Prints out grades if name exist in dictionary
    if studentName4 in studentDictionary:
      print(f"{studentName4} grades are {studentDictionary[studentName4]}")
    else:
      print(f"{studentName4} does not exist")

# Get studen'ts letter grade
  elif userInput == "5":
    studentName5 = input("Enter a student name: ")
    if studentName5 in studentDictionary:
# Calculate average of student's grade
      Average = sum(studentDictionary[studentName5]) / len(studentDictionary[studentName5])
# Gives student's grade based on average
      if Average >= 90:
        print(f"{studentName5}'s current grade is an A")
      elif Average >= 80:
        print(f"{studentName5}'s current grade is a B")
      elif Average >= 70:
        print(f"{studentName5}'s current grade is a C")
      elif Average >= 60:
        print(f"{studentName5}'s current grade is a D")
      elif Average >= 50:
        print(f"{studentName5}'s current grade is an E")
      else:
        print(f"{studentName5}'s current grade is an F")
        
# Ends loop    
  else:
    print("Grade input has shutdown")
      
  
