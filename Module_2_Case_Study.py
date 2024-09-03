print("Welcome to my Dean's list and Honor Roll Calculator!\n"
      "Please know that all information given will comply with school privacy standards.")
while True:
    last_name = input("If you would like to quit the program please enter ZZZ\n"
                      "Please enter your last name: \n")
    if last_name == "ZZZ":
        break
    first_name = input("Please enter your first name: \n")
    
    while True:    
        try:
            gpa = float(input("Please enter your current GPA: "))
        except ValueError:
            print("Please enter you GPA as numeric value!")
        else:
            break
    
    if gpa >= 3.5:
        print(f"Congratulations {first_name} {last_name} you made the Dean's List")
    elif gpa >= 3.25:
        print(f"Congratulations {first_name} {last_name} you made the Honor Roll")
    else:
        print(f"Sorry {first_name} {last_name} you didn't make the Dean's List or Honor Roll")