import validators
import csv
#print(validators.input_postal_code("Please enter your postal code (Enter 'q' to quit): ", 1010, 1020, 1030))
#print(validators.input_bounded_integer("Please enter ", "age", 0, 130))
person = {"name": None, "Day":None,"month":None,"year":None,"postal":None}
while True:
    selection = input( "Please choose which aspect to edit: (n)ame, (d)ay of birth, (m)onth of birth, (y)ear of birth, (p)ostal code (or enter 'q' to quit):").upper()

    match selection:
        case "NAME" | "N":
            #print (validators.input_string("Please Enter Name, Enter Q to Quit: "))
            person["name"]= validators.input_string("Please Enter Name, Enter Q to Quit: ")
        case "DAY OF BIRTH" | "DAY" | "D":
            #print(validators.input_bounded_integer("Please Enter ", "Day of birth", 1, 31))
            person["Day"]=validators.input_bounded_integer("Please Enter ", "Day of birth", 1, 31)
        case "MONTH OF BIRTH" | "MONTH" | "M":
            #print(validators.input_bounded_integer("Please Enter ", "Month of birth", 1, 12))
            person["month"]=validators.input_bounded_integer("Please Enter ", "Month of birth", 1, 12)
        case "YEAR OF BIRTH" | "YEAR" | "Y":
            #print(validators.input_bounded_integer("Please Enter ", "Year of birth", 1850, 2022))
            person["year"]=validators.input_bounded_integer("Please Enter ", "Year of birth", 1850, 2022)
        case "POSTAL CODE" | "POSTAL" | "P":
            #print(validators.input_postal_code("Please enter your postal "
                                              #"code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040, 1050))
            person["postal"]=validators.input_postal_code("Please enter your postal "
                                               "code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040, 1050)
        case "QUIT" | "Q":
            break
        case _:
            print("Not valid option! Please try it again!")


with open('people.csv', 'w', newline='', encoding="UTF-8") as csvfile:
         writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
         key_list = list (person.keys())
         writer.writerow(person.keys())
         writer.writerow([person["name"],person["Day"], person["month"], person["year"],person["postal"]])

print(person)
print("Thank you for using the Validator!")