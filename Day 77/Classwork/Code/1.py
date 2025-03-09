def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age > 0:
        if age == 1:
            return f"You are 1 year old."
        else:
            return f"You are {age} years old."
    elif age < 0:
        if age == -1:
            return f"You will be born in 1 year."
        else:
            return f"You will be born in {-age} years."
    else:
        return "You were born this very year!"
    