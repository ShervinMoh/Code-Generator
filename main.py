import random

def main():
    try:
        selection = int(input("""What should your password be?\nPlease enter the desired number
        1-Letters
        2-Letters & Numbers
        3- Letters & Numbers & Special Characters\n"""))

        entry = int(input("How many characters should be in your password? "))

        print(system(selection, entry))

    except ValueError:
        print("You must choose one of the available options!")

def system(selection, entry):
    password = ""
    if selection in range(1,4):
        if entry <= 15:
            if selection == 1:
                while len(password) != entry:
                    character = letter_generator()
                    
                    password = password + character
                return password
            
            elif selection == 2:
                while len(password) != entry:
                    chance = random.randint(0,1)

                    if chance == 0:
                        character = letter_generator()
                    elif chance == 1:
                        character = number_generator()

                    password = password + character
                return password
            
            elif selection == 3:
                while len(password) != entry:
                    chance = random.randint(0,2)

                    if chance == 0:
                        character = letter_generator()
                    elif chance == 1:
                        character = number_generator()
                    elif chance == 2:
                        character = special_character_generator()

                    password = password + character
                return password
        else:
            return "The maximum limit is 15 characters!"
    else:
        return "You must choose one of the available options!"

def letter_generator():
    letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    target_letter = random.choice(letter)
    return target_letter

def number_generator():
    number = '0123456789'
    target_number = random.choice(number)
    return target_number

def special_character_generator():
    special_character = '!@#$%'
    target_special_character = random.choice(special_character)
    return target_special_character

if __name__ == "__main__":
    main()