import validators
import csv

person = {"Name": None, "Day": None, "Month": None, "Year": None, "Postal": None}
while True:
    selection = input(
        "Please choose which aspect to edit: (n)ame, (d)ay of birth, (m)onth of birth, (y)ear of birth, (p)ostal code (or enter 'q' to quit):").upper()

    match selection:
        case "NAME" | "N":
            person["Name"] = validators.input_string("Please Enter Name, Enter Q to Quit: ")
        case "DAY OF BIRTH" | "DAY" | "D":
            person["Day"] = validators.input_bounded_integer("Please Enter ", "Day of birth", 1, 31)
        case "MONTH OF BIRTH" | "MONTH" | "M":
            person["Month"] = validators.input_bounded_integer("Please Enter ", "Month of birth", 1, 12)
        case "YEAR OF BIRTH" | "YEAR" | "Y":
            person["Year"] = validators.input_bounded_integer("Please Enter ", "Year of birth", 1850, 2022)
        case "POSTAL CODE" | "POSTAL" | "P":
            person["Postal"] = validators.input_postal_code("Please enter your postal "
                                                            "code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040, 1050)
        case "QUIT" | "Q":
            break
        case _:
            print("Not valid option! Please try it again!")

answer=""

while answer.upper() != "Q":
    try:
        with open('people.csv', 'w', newline='', encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(person.keys())
            writer.writerow([person["Name"], person["Day"], person["Month"], person["Year"], person["Postal"]])
            answer="Q"
    except PermissionError:
        print("\ncsv file exists and open. Please close the file!")
        answer=input("\nPlease press Enter if you closed the file or (Q) to quit! : ")

print(person)
print("Thank you for using the Validator!")
