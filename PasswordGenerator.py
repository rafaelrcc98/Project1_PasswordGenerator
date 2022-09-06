
# GLOBAL ITEMS________________________________________
from PasswordTools import *
import random

user_password = Password([],[],[])
# END GLOBAL ITEMS____________________________________



# Prints intro message
print("Wellcome to PasswordGenerator. This program will generate a randomized password of chosen length and "
      "complexity. \n \n")

# Obtaining the length of the password
loopend = False
while loopend == False:
    try:
        print("First, how long would you like your password to be?\n")
        user_password.length = PassLength("Insert the number of characters: ")
        print("Password will be " + str(user_password.length) + " characters long...")
        loopend = True
    except:
        print("\n!! Please input only whole numbers !!\n")

# Obtaining the complexity
loopend = False
while loopend == False:
    try:
        print("How complex would you like your password to be?\n")
        print("0: Password contains numbers (1234)")
        print("1: Password contains numbers and lowercase letters (1a2b)")
        print("2: Password contains numbers, lowercase letters, and uppercase letters (1aA2)")
        print("3: Password contains numbers, lower and uppercase letters, and special characters (1aA!)\n")
        user_password.complexity = int(input("Select an option from 0 to 3: "))
        compl_options = [0, 1, 2, 3]
        if user_password.complexity in compl_options:
            loopend = True
        else:
            print("\n !! Number chosen is outside of range !!\n")
    except:
        print("\n!! Please input only whole numbers !!\n")

# Generating Password
for character in range(user_password.length):
    user_password.content.append(random.choice(randomChar[str(user_password.complexity)]))

# Converting into nice string and printing
user_password.content = (''.join(user_password.content))
print("\nYour randomly generated password is: " + str(user_password.content) + "\n")

# Asking if password should be saved in a text file
loopend = False
while loopend == False:
    print("Would you like to save this into a text file?")
    ans1 = input("[y] [n]: ")
    if ans1 in UserAnswers['y']:
        save = True
        loopend = True
    elif ans1 in UserAnswers['n']:
        print("Ok, password will not be saved.")
        save = False
        break
    else:
        print("Invalid answer, please answer 'y' or 'n' \n")

# Saving the file in the same path as current directory
loopend = False
if save == True:
    while loopend == False:
        try:
            import os.path
            filename = input("\nName of file: ")
            print("Attempting to create file... \n")
            filename.join('.txt')
            # Checking to see if filename chosen is already in use
            while os.path.isfile(filename) == True:
                print("Looks like this filename is already taken, would you like to override this file?")
                ans2 = input("[y] [n]: ")
                if ans2 in UserAnswers['y']:
                    print("Ok, file will be overridden...\n")
                    break
                elif ans2 in UserAnswers['n']:
                    print("File will not be overridden. Please enter new name.")
                else:
                    print("Invalid answer, please answer 'y' or 'n' \n")
                filename = input("Name of file: ")
                print("Attempting to create file... \n")
                filename.join('.txt')
            f = open(filename, 'w')
            f.write("Below is the password you generated using the PasswordGenerator program. \n\n")
            f.write("Your password is: " + user_password.content)
            f.close()
            print("File was successfully created under the name '" + filename + "' It is located in the same "
                                                                                "directory as this program.")
            loopend = True
        except:
            print("!! A problem occurred and the file could not be created !!")
            print("Would you like to try again?")
            ans3 = input("[y] [n]: ")
            if ans3 in UserAnswers['n']:
                print("Ok, will not attempt to save password again.")
                loopend = True

print("Program has concluded successfully!")
# END
