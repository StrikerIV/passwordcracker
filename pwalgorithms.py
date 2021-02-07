
import itertools
import string
import re

guesses = 0

# get words


def get_dictionary():
    words = []
    dictionary_file = open("dictionary.txt")
    for line in dictionary_file:
        words.append(line[:-1].lower())
    dictionary_file.close()
    return words

# get non-alphanumeric characters


def get_nonalpha():
    characters = string.printable
    non_alpha = re.findall("[^a-zA-Z\d\s]", characters)
    print(non_alpha)
    return non_alpha

# find all words in dictionary


def find_words(password):
    words = get_dictionary()
    matched_words = []
    for word in words:
        global guesses
        guesses += 1
        # loop through all words to find matches
        if word in password:
            matched_words.append(word)

    return matched_words


def crack_password(password):
    global guesses

    password = password.lower()
    found_words = find_words(password)
    length = len(password)

    found_words.sort(key=len, reverse=True)

    for i in range(length):
        for combination in itertools.combinations(found_words, i):

            passwordcrack = password

            for comb in combination:
                passwordcrack = passwordcrack.replace(comb, "")
                guesses += 1

                if passwordcrack:
                    if not re.findall("[a-zA-Z]+", passwordcrack):
                        print(passwordcrack)
                        if re.findall("[0-9]+", passwordcrack):
                            print(re.findall("[0-9]+", password))
                            # has numbers

                            solved_numbers = []
                            numbers = re.findall("[0-9]+", password)
                            solved = 0
                            count = -1

                            for index, num in enumerate(numbers):
                                numbers[index] = int(num)

                            while solved != len(numbers):
                                count += 1
                                guesses += 1

                                if count in numbers:
                                    solved_numbers.append(count)
                                    passwordcrack = passwordcrack.replace(
                                        str(count), "")
                                    solved += 1

                            combination = combination + tuple(solved_numbers)

                        if re.findall("[^a-zA-Z\d\s]", passwordcrack):
                            # has non-alphanumeric characters

                            non_alpha_found = re.findall(
                                "[^a-zA-Z\d\s:]", passwordcrack)

                            solved_chars = []
                            non_alpha = get_nonalpha()
                            solved = 0
                            count = 0

                            while solved != len(non_alpha_found):
                                if count >= len(non_alpha):
                                    break
                                elif non_alpha[count] in non_alpha_found:
                                    solved_chars.append(non_alpha[count])

                                    passwordcrack = re.sub(
                                        str(non_alpha[count]), "", passwordcrack)
                                    passwordcrack = passwordcrack.replace(
                                        non_alpha[count], "")

                                    solved += 1

                                count += 1
                                guesses += 1

                            if not passwordcrack:
                                combination = combination + tuple(solved_chars)
                                return guesses, combination
                            else:
                                return guesses, "not_found"
                        else:
                            return guesses, combination

                else:
                    return guesses, combination
    return guesses, "not_found"

# returned = crack_password("kookykoala10")
# print(returned)
