#Story introduction
print("~~ Batman's Bootcamp ~~\n\n"
"                    ***********************\n"
"               *********************************\n"
"           *******   *     *       *    *    *******\n"
"        *******   ***      **     **     ***   *******\n"
"      ******   *****       *********      *****    *****\n"
"    ******  ********       *********       ******    *****\n"
"   ****   **********       *********       *********   *****\n"
"  ****  **************    ***********     ************   ****\n"
" ****  *************************************************  ****\n"
"****  ***************************************************  ****\n"
"****  ****************************************************  ****\n"
"****  ****************************************************  ****\n"
" ****  ***************************************************  ****\n"
"  ****  *******     ****  ***********  ****     *********  ****\n"
"   ****   *****      *      *******      *      ********  ****\n"
"    *****   ****             *****             ******   *****\n"
"      *****   **              ***              **    ******\n"
"       ******   *              *              *   *******\n"
"         *******                                *******\n"
"            ********                         *******\n"
"               *********************************\n"
"                    ***********************")

print("\nBatman has appointed you, Kakapo, as his new official sidekick. He is putting you through weapon selection to determine your special abilities and whether you are up to the real world challenge")

print("\nWith options in front of you, your selection will determine whether you will be fighting crimes through the screen or in the streets")

#Selecting your first path
print("\n You walk into the Batcave with Batman looks over your shoulder. You both walk up to a glass display case with three items inside. He says 'Kakapo, what will you choose?'\n"
     "  A. You choose a crystal ball with a strange purple glow\n"
     "  B. You choose a dual blade sword, each emitting a red hot glow\n"
     "  C. You choose the wooden staff, which looks like it was carved out of an ancient tree\n")
choiceOne = input("Which weapons calls your name? Please select option A-C: ")

#Choice selection
#Journey of the crystal ball
if choiceOne == "A":
  print("\n---------------------------------------------------")
  print("\nYou hear the crystal ball call out your name and your mind fogs up. A math question appears. 'What is 5 x (8+2)?' ")
  choiceOneAnswer = input("What is your answer: ")
#Journey of the crystal ball answer
  if choiceOneAnswer == "50":
    print("\nYou have obtained psychic abilities, being able to read minds and telekinetic powers. Batman gives you a bombastic side-eye as you levitate him from his position.")
  else:
    print("\nYou wake up in the hospital with a headache. Maybe you aren't cut out for this.")
    
#Journey of the dual blade
elif choiceOne == "B":
  print("---------------------------------------------------")
  print("\n The swords grow brighter as you reach out to touch them. What emotions are you feeling?\n")
#Journey of the dual blade options
  print("  A. You feel angry, hot, and sweaty as you touch the swords, turning the sword red\n"
      "  B. You feel calm, unbothered by the heat and sweat, grabbing the sword that turns red\n")
  choiceTwo = input("What do you feel? Please select option A or B: ")
  if choiceTwo == "A":
    print("\nUncontrollable flames start coming out of the sword, which sets off the sprinkler in the Batcave. Water rains down. Batman stares and says 'Drop it, you will be cleaning this up.'")
  else:
    print("\nThe sword feels light in your hand has you swing at a dummy, setting it to flames. 'Looks like you got a knack for it Kakapo', says Batman")
    
#Journey of the staff
elif choiceOne == "C":
  print("---------------------------------------------------")
  print("\nBatman says 'That's Alfred's walking staff. You best learn Python and gather crime statistics from the Batcave Kakapo.")
else:
  print("Try again")