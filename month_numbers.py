#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds if a number is associated with a month


def main():
    # Finds if a number is associated with a month

    month_number = int(input("Enter a month number: "))
    match month_number:
        case 1:
            month = "January"
        case 2:
            month = "February"
        case 3:
            month = "March"
        case 4:
            month = "April"
        case 5:
            month = "May"
        case 6:
            month = "June"
        case 7:
            month = "July"
        case 8:
            month = "August"
        case 9:
            month = "September"
        case 10:
            month = "October"
        case 11:
            month = "November"
        case 12:
            month = "December"
        case _:
            month = "nothing"
    print("\nThe month number for {0} is {1}.".format(month_number, month))

    print("\nDone.")


if __name__ == "__main__":
    main()
