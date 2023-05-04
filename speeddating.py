#ASCII Art Title
print(r"""
                                                                 
                       (       (             )                   
              (    (   )\ )    )\ )    )  ( /( (          (  (   
 (   `  )    ))\  ))\ (()/(   (()/( ( /(  )\()))\   (     )\))(  
 )\  /(/(   /((_)/((_) ((_))   ((_)))(_))(_))/((_)  )\ ) ((_))\  
((_)((_)_\ (_)) (_))   _| |    _| |((_)_ | |_  (_) _(_/(  (()(_) 
(_-<| '_ \)/ -_)/ -_)/ _` |  / _` |/ _` ||  _| | || ' \))/ _` |  
/__/| .__/ \___|\___|\__,_|  \__,_|\__,_| \__| |_||_||_| \__, |  
    |_|                                                  |___/ 
    """)

#Introduction and instructions
print("Welcome to Speed Dating, a quiz where you are asked 5 True or False statements. If all 5 answers matches our lucky candidate, Batman, you get to go on a date with him. Please ONLY enter the letter T or F (case-sensitive) when it's your turn to answer.")

print("\n~~~~~~May you find Batman in your future~~~~~~\n")

#Setup Questions and Answers
questions = ("  Q1. You are an extrovert" , "  Q2. You enjoy dancing" , "  Q3. You consider yourself an outdoor fanatic" , " Q4. You cook very well" , "  Q5. You get along well with your family")
answers = ("T" , "T", "T", "F", "F")
score = 0


#Calculate the number of questions
numberOfQuestions = len(questions)

#Loop once for each questions
for index in range (numberOfQuestions):
  print(questions[index])
  userGuess = ""

#Loop for correct input
  while (userGuess != "T" and userGuess != "F"):
    userGuess = input("Please enter 'T' for True or 'F' for False: ")

#Add counter if answer is correct
  if(userGuess == answers[index]):
    score += 1

#Results of quiz

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if (score < 5):
  print(f"\nUnfortunately, you aren't compatible with Batman. You only matched {score} statements")
else:
  print(f"\nCongratulations, you are a perfect match! Batman is waiting for you in his Batmobile")
  print(r"""
          .  .
          |\_|\
          | a_a\
          | | "]
      ____| '-\___
     /.----.___.-'\
    //        _    \
   //   .-. (~v~) /|
  |'|  /\:  .--  / \
 // |-/  \_/____/\/~|
|/  \ |  []_|_|_] \ |
| \  | \ |___   _\ ]_}
| |  '-' /   '.'  |
| |     /    /|:  | 
| |     |   / |:  /\
| |     /  /  |  /  \
| |    |  /  /  |    \
\ |    |/\/  |/|/\    \
 \|\ |\|  |  | / /\/\__\
  \ \| | /   | |__
snd    / |   |____)
       |_/)
  """)
    
    
    