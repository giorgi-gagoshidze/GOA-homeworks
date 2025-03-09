def the_information():
    ask = input("Do you want to see information about atributte split()? (yes/no): ")

    if ask == "yes":
        print("#split() in Python# The split() method is used to divide a string into a list of substrings based on a specified separator. If no separator is provided, it defaults to splitting by whitespace. This method returns a list of the separated elements. An optional parameter, maxsplit, can be used to limit the number of splits performed.")
    elif ask == "no":
            print("try again to make sure")
            the_information()
    else:
        print("enter yes/no please (enter yes or no please)")
the_information()