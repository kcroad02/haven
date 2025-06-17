import random
import time
from save import *
# Imports savefile data from save.py

# Main menu
init0=("Haven Town\nROGBONE\n\nEnter C to Continue\n\nEnter N for New Game\n\n")


# Beginning texts
init1 = "\n\nHaven Town\nROGBONE\n\nAliens have depleted Earth of its resources and left behind creatures known as xenomorphs, which humanity has befriended, in order to save themselves from the brink of extinction."
init2 = "\nAs one of the lone survivors, you must travel to Haven Village to meet with the others, but you will first have to traverse...\n\nThe Forest."
init3 = "\nYou awaken from your slumber in your makeshift home, a tent of tree limbs and leaves, your xenomorph pet by your side.\nWhat was her name again?\n"


# Used so I don't have to retype that everytime.
inputContinue = "\n\nInput to continue"


answer = ""
running = True
enemiesKilled = 0



# Different every time, framework for the enemies
class enemy():
    def __init__(self, name, health, maxhealth, damage, move, move2):
        self.name = name
        self.health = health 
        self.maxhealth = maxhealth
        self.damage = damage
        self.move = move
        self.move2 = move2

        
# Enemy list
steelwulf = enemy("Steelwulf", 100, 100, 15, "Slash", "Steel Claw")
warpdemon = enemy("Warpdemon", 23, 100, 25, "Blarp", "Timewarp")


def save():
    f = open("save.py", "w")
    f.write("petname = \"" + petname +"\"\n")
    f.write("health = " + str(health) +"\n")
    f.write("maxhealth = " + str(maxhealth)+"\n")
    f.write("damage = " + str(damage)+"\n")
    f.write("movename =\"" + movename+"\"\n")
    f.write("movename2 =\"" + movename2+"\"\n")
    f.write("stage = " + str(stage)+"\n")
    f.close()
    print("******** Saved *********")
    
def confirmName():
  global petname
  petname = input("Enter your xenomorph's name:\n")
  answer = input(petname + "? Y or N\n")
  if answer.upper() == "Y" and petname != "":
   print("Pet name confirmed as " + petname + "\n")
  else:
    confirmName()

def stepDrama():
  num = 0
  while num < 3:
    print("\n+1 mile traversed")
    time.sleep(0.5)
    num = num + 1
    
    
def levelUp():
    global enemiesKilled
    global maxhealth
    global health
    global damage
    healthQ = input("You have protected yourself against " + str(enemiesKilled) + " xenomorph(s)\n\nWould you like to level up your health?\n\nY or N\n")
    if healthQ.upper() == "Y":
        maxhealth = maxhealth + (enemiesKilled * 2)
        print("Your max health is now " + str(maxhealth))
    elif healthQ.upper() == "N":
        damageQ = input("\nWould you like to level up your damage instead?\n\nY for Yes or N for No\n")
        if damageQ.upper() == "Y":
            damage = damage + (2*enemiesKilled)
            print("Your damage is now at " + str(damage))
        else:
            print("Skipped leveling up.")
            return
    else:
        levelUp()
  
def yOrN(answer):
    if answer.upper() == "Y":
        return True
    if answer.upper() == "N":
        return False
    else:
        yOrN(answer)
    
def fight(enemy):
  # Doesn't work without earlier referenced variables being global'd
  # The fighting mechanic
  global health
  global petname
  global damage
  global maxhealth
  global enemiesKilled
  while health > 0 and enemy.health > 0:
    askFight = input("\n" + petname + " Health: " + str(int(health)) + "/" + str(maxhealth) + "\n" + enemy.name + " Health: " + str(int(enemy.health)) + "/" + str(enemy.maxhealth) + "\nEnter 1 to use " + movename + " (1x damage)\nEnter 2 to use " + movename2 + " (2x damage)\n\n")
    
    # option 1
    if askFight == str(1):
        number = input("\nAttempt to guess a number between 1 and 10 better than the opponent\n\n")
        if number.isdigit():
          number = int(number)
        else:
          fight(enemy)
        
        number = int(number)
        numAns = random.randrange(1,10)  
        enemyAns = random.randrange(1,10)
        
        
        if number - numAns > enemyAns - numAns:
          enemy.health -= damage
          print("\nYou selected a closer number!\n" + petname + " used " + movename + "\n")
          
          if number - numAns == -1 or number - numAns == 3:
            print("Critical hit! 1.5x damage applied")
            enemy.health -= 1.5 * (damage)
            
        elif number - numAns < enemyAns - numAns:
          health -= enemy.damage
          print("\n" + enemy.name + " has selected a better number\n" + enemy.name + " used " + enemy.move)
        else:
           print("\nA stalemate!")
        

    # option 2, risky
    if askFight == str(2):
        print("Rolling dice")
        time.sleep(0.3)
        print("...")
        time.sleep(0.3)
        print("...")
        dice = random.randrange(1,6)
        
        if dice == 1:
            print("You rolled a " + str(dice) + "!\n75% of " + enemy.name +"'s health is gone!")
            enemy.health -= 0.75 * enemy.health
        elif dice == 2:
            print("You rolled a " + str(dice) + "!\n" + petname + " hurt herself in confusion!")
            health -= 0.2*(enemy.damage)
        elif dice == 3:
            print("You rolled a " + str(dice) + "!\nNothing happened!")
        elif dice == 4:
            print("You rolled a " + str(dice) + "!\n" + petname + " left herself open to an attack, but countered it!")
            health -= 0.5*enemy.damage
            enemy.health -= damage
        elif dice == 5:
            print("You rolled a " + str(dice) + "!\n" + petname + " missed the enemy " + enemy.name+"!")
        elif dice == 6:
            print("You rolled a " + str(dice) + "!\n75% of " + enemy.name +"\'s health is gone!")
            enemy.health -= 0.75 * enemy.maxhealth
        
  if enemy.health <= 0:
    print("\nYou have won the battle against " + enemy.name + "!\n")
    health = maxhealth
    enemy.health = enemy.maxhealth
    enemiesKilled += 1
  elif health <= 0:
    print("\nYour xenomorph has lost all health!\n\nGame over.")
    quit()






cONTrue = True
while cONTrue:

    continueOrNew = input(init0)

    if continueOrNew.upper() == "N":
        petname = ""
        health = 100
        maxhealth = 100
        damage = 50
        movename = "Chomp"
        movename2 = "Buzz"
        stage = 0
        cONTrue = False
    elif continueOrNew.upper() == "C":
        cONTrue = False
    else:
        pass

# while game is running
while running:

    if stage == 0:

        input(init1 + inputContinue)
        input(init2 + inputContinue)
        print(init3)

        confirmName()
        stage = 1
        save()

    elif stage == 1:
        txt0 = "\nYou emerge into the cool-weathered and dark world of The Forest. Despite being populated by millions of creatures, you can only hear the rustling of your and " + petname + "'s footsteps.\n"
        input(txt0 + inputContinue)
        stepDrama()
        txt1 = "\nYou trek deeper and deeper - until suddenly..."
        input(txt1+ inputContinue)
        enemyChoice = random.randrange(1,10)
        if enemyChoice == 3 or enemyChoice == 7 or enemyChoice == 4 or enemyChoice == 2:
            fighter = warpdemon
        else:
            fighter = steelwulf
        hasAppeared = "\nA " + fighter.name + " has appeared!"
        input(hasAppeared + inputContinue)
        fight(fighter)
        levelUp()
        stage = 2
        save()
    
    elif stage == 2:
        txt2 = input("\nYou stumble upon a tattered journal layed upwards on a tree\n\nDo you open it?\nY or N: ")
        if yOrN(txt2) == True:
            input("Test DEEZ NUTS BOY YEYEYEYEAHHAH LOL! \n\n" + inputContinue)
        stepDrama()
        stage = 3
        save()
    
    
    elif stage == 3:
        stepDrama()
        enemyChoice = random.randrange(1,10)
        if enemyChoice == 3 or enemyChoice == 7 or enemyChoice == 4 or enemyChoice == 2:
            fighter = warpdemon
        else:
            fighter = steelwulf
        hasAppeared = "\nA " + fighter.name + " has appeared!"
        input(hasAppeared + inputContinue)
        fight(fighter)
        levelUp()
        txt4 = "\nYou trek onward to Haven Village..."
        input(txt4 + inputContinue)
        stage = 4
        save()
    elif stage == 4:
        txt5 = "\nI don't have anything else made yet LOL"
        input(txt5 + inputContinue)
        stage = 5
        save()
        running = False
    else:
        print("Error: Please try reinstalling game files to continue.")

quit()