# Daniel Alvarez, Juan Bravo, Ramazan Tolonbaev
# 10/17/23
# Team Activity Module 4

# Prompts the User to select a fruit to eat and informs them if the fruit they ate is healthy and poisonous

# Asks the user to type their name before moving on to the next challenge
username = input("Please tell me your name before continuing with the challenge:")

# Greets the User with their name and then prompts the user to select a fruit
print("Hello {}, you must select a fruit to eat.".format(username))

# Warns the user to choose wisely as half of the fruits have poison
print("Choose wisely as 3 out 6 of the fruits have poison inside of them.")

# Provides a list of 6 fruits that the user can select
print(" 1. Orange\n 2. Apple\n 3. Watermelon\n 4. Banana\n 5. Pineapple\n 6. Mango")

# Asks the user to select a number that is assigned to the fruit
user_option = int(input("Please select the number of the fruit you would like to eat:"))

# If the user selects fruit numbers 1,4,or 6 then the user will have a message saying they will live a happy life
if user_option == 1 or (user_option == 4) or (user_option == 6):
    print("You chose option {}, and it looks like you will live a happy and healthy life!".format(user_option))

# If the user selects fruit numbers 2,3, or 5 then the user will have a message saying they will have 24 hours to live
elif user_option == 2 or (user_option == 3) or (user_option == 5):
    print("You chose option {}, and it looks like you only have 24 hours left to live!".format(user_option))

# If the user chooses a fruit number that is not 1-6 then will have message saying to renter a number that from 1-6
else:
    print("Please select a fruit option between 1-6")