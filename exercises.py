def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

print_greeting()


def check_letter():
    letter = input('Enter a letter: ')

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    if letter.lower() in vowels:
        print(f'The letter {letter} is a vowel.')
    elif letter.lower() in consonants:
        print(f'The letter {letter} is a consonant.')
    else:
        print('That is not a valid letter. Please enter one letter (a-z).')

check_letter()


def check_voting_eligibility():
    VOTING_AGE = 18

    try:
        age = int(input('Please enter your age: '))

        if age < 0:
            print('Invalid age. Age cannot be a negative number.')
        elif age >= VOTING_AGE:
            print('You are eligible to vote.')
        else:
            print('You are not eligible to vote yet.')
    except ValueError:
        print('Invalid input. Please enter a whole number for your age.')

check_voting_eligibility()


def calculate_dog_years():
    dog_age = int(input("Input a dog's age: "))

    if dog_age < 0:
        print('Invalid age. Age cannot be a negative number.')
    elif dog_age < 3:
        dog_years = dog_age * 10
        print(f"The dog's age in dog years is {dog_years}.")
    else:
        dog_years = 20 + (dog_age - 2) * 7
        print(f"The dog's age in dog years is {dog_years}.")

calculate_dog_years()


def weather_advice():
    is_cold = input('Is it cold? (yes/no): ').lower() == 'yes'
    is_raining = input('Is it raining? (yes/no): ').lower() == 'yes'

    if is_cold and is_raining:
        print('Wear a waterproof coat.')
    elif is_cold and not is_raining:
        print('Wear a warm coat.')
    elif not is_cold and is_raining:
        print('Carry an umbrella.')
    else:
        print('Wear light clothing.')

weather_advice()
