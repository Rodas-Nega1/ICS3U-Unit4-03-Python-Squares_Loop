# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sept 2021
# This program asks for a number, then checks if it is
# less than or equal to the user number by continuously squaring itself


def main():
    # this function loops until it is less than or equal to the user integer
    # and creates a squares sequence

    # input
    user_number = input("Enter in a positive integer: ")
    print("")

    # process & output
    try:

        user_number_int = int(user_number)

        if user_number_int < 0:
            print("That is an invalid integer.")

        for square_loop in range(user_number_int + 1):
            result = square_loop * square_loop
            print("{0}² = {1}".format(square_loop, result))

    except Exception:
        print("That is an invalid integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
