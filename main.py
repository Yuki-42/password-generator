import random
import char
import logging
import sys


# Initialising logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s:%(levelname)s:%(message)s',
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


def createPassword(length, lowercase, capitals, numbers, specials, filePrint):
    choices = []
    if lowercase:
        choices.append("lowercase")
        logging.info("lowercase appended")

    if capitals:
        choices.append("capitals")
        logging.info("capitals appended")

    if numbers:
        choices.append("numbers")
        logging.info("numbers appended")

    if specials:
        choices.append("specials")
        logging.info("specials appended")

    logging.debug(choices)

    password = ""

    for i in range(length):
        choice = random.choice(choices)
        logging.debug(f"choice: {str(choice)}")

        match choice:
            case "lowercase":
                character = random.choice(char.lowercase)
                logging.debug(f"character: {str(character)}")
                password = password + character

            case "capitals":
                character = random.choice(char.capitals)
                logging.debug(f"character: {str(character)}")
                password = password + character

            case "numbers":
                character = random.choice(char.numbers)
                logging.debug(f"character: {str(character)}")
                password = password + character

            case "specials":
                character = random.choice(char.specials)
                logging.debug(f"character: {str(character)}")
                password = password + character

    return password


def fullExit():
    # root.destroy()
    exit()


def updateSliderLabel(var):
    print(var)


if __name__ == '__main__':
    print("Welcome to GENERIC_PASSWORD_MAKER")

    inputLength = input("How long would you like your password to be in digits? ")
    try:
        _ = int(inputLength)
    except ValueError:
        print("Invalid length input, try again.")
        inputLength = input("How long would you like your password to be in digits? ")
        try:
            _ = int(inputLength)
        except ValueError:
            exit("Funny guy, huh?")

    inputCapitals = input("Would you like to use capitalsAllowed in your password? y/n ")
    if inputCapitals == "yy":
        inputCapitals = "y"
        inputNumbers = "y"
        inputLowercase = "y"
        inputSpecials = "y"
        inputOutputToFile = "y"
        logging.info("Yes to all options selected")

    else:
        inputNumbers = input("Would you like to use numbersAllowed in your password? y/n ")
        inputLowercase = input("Would you like to use lowercase letters in your password? y/n ")
        inputSpecials = input("Would you like to use special characters and symbols in your password? y/n ")

        inputOutputToFile = input("Do you want to output to a text file? y/n ")

    # Determine bool for capitalsAllowed
    if inputCapitals == "y":
        capitalsAllowed = True

    elif inputCapitals == "n":
        capitalsAllowed = False

    else:
        print("Invalid input, assuming Yes")
        capitalsAllowed = True

    # Determine bool for numbersAllowed
    if inputNumbers == "y":
        numbersAllowed = True

    elif inputNumbers == "n":
        numbersAllowed = False

    else:
        print("Invalid input, assuming Yes")
        numbersAllowed = True

    # Determine bool for lowercaseAllowed
    if inputLowercase == "y":
        lowercaseAllowed = True

    elif inputLowercase == "n":
        lowercaseAllowed = False

    else:
        print("Invalid input, assuming Yes")
        lowercaseAllowed = True

    # Determine bool for specialsAllowed
    if inputSpecials == "y":
        specialsAllowed = True

    elif inputSpecials == "n":
        specialsAllowed = False

    else:
        print("Invalid input, assuming Yes")
        specialsAllowed = True

    # Determine bool for fileOut
    if inputOutputToFile == "y":
        fileOut = True

    else:
        fileOut = False

    # Create Password
    try:
        output = createPassword(int(inputLength), capitalsAllowed, numbersAllowed, lowercaseAllowed, specialsAllowed,
                                fileOut)
    except ValueError:
        logging.error(f"int(inputLength) produces ValueError, inputLength = {inputLength}")
        exit("Password Length input is invalid")
    if not fileOut:
        print(f"Password: {output}")
    else:
        with open("output.txt", "w") as file:
            # Wiping Old File
            file.truncate()
            # Writing New Password
            file.write(output)

    if len(output) == int(inputLength):
        logging.debug("len(output) == int(inputLength)")
    else:
        logging.error("OUTPUT LENGTH DOES NOT MEET DESIRED LENGTH")
