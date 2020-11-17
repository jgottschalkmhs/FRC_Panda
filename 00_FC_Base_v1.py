# import libraries


# *** Functions go here ****

# checks that input is either a float or an
# integer that is more than zero
def num_check(question, num_type):
    valid = False

    # error depends on type
    if num_type == float:
        error = "Please enter a number that is more than zero\n"
    else:
        error = "Please enter an integer (whole number) " \
                "that is more than zero\n"

    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Checks that user has entered yes / no to a question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Please enter either yes or no...\n")


# **** Main Routine goes here ****
