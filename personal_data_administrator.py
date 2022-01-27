import validators
import csv

class Person:
    def __init__(self, name, day, month, year, postal):
        # creation of attribute (instance variable) name
        self.name = name
        self.day = day
        self.month = month
        self.year = year
        self.postal = postal

person = {"Name": None, "Day": None, "Month": None, "Year": None, "Postal": None}
while True:
    selection = input(
        "Please choose which aspect to edit: (n)ame, (d)ay of birth, (m)onth of birth, (y)ear of birth, (p)ostal code (or enter 'q' to quit):").upper()

    match selection:
        case "NAME" | "N":
            Person.name = validators.input_string("Please Enter Name, Enter Q to Quit: ")
        case "DAY OF BIRTH" | "DAY" | "D":
            Person.day = validators.input_bounded_integer("Please Enter ", "Day of birth", 1, 31)
        case "MONTH OF BIRTH" | "MONTH" | "M":
            Person.month = validators.input_bounded_integer("Please Enter ", "Month of birth", 1, 12)
        case "YEAR OF BIRTH" | "YEAR" | "Y":
            Person.year = validators.input_bounded_integer("Please Enter ", "Year of birth", 1850, 2022)
        case "POSTAL CODE" | "POSTAL" | "P":
            Person.postal = validators.input_postal_code("Please enter your postal "
                                                            "code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040, 1050)
        case "QUIT" | "Q":
            break
        case _:
            print("Not valid option! Please try it again!")

p1 = {"Name": Person.name, "Day": Person.day,"Month": Person.month, "Year": Person.year, "Postal": Person.postal}
print (p1)
answer=""

while answer.upper() != "Q":
    try:
        with open('people.csv', 'w', newline='', encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(p1.keys())
            writer.writerow([p1["Name"], p1["Day"], p1["Month"], p1["Year"], p1["Postal"]])
            answer="Q"
    except PermissionError:
        print("\ncsv file exists and open. Please close the file!")
        answer=input("\nPlease press Enter if you closed the file or (Q) to quit! : ")

print(person)
print("Thank you for using the Validator!")
