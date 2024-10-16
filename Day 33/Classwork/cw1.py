#შექნენით ფუნქცია რომელიც გადააქცევს celsius fahrenheit-ად (პირიქითაც შეგიძლიათ)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_in_fahrenheit = celsius_to_fahrenheit(25)
print(temp_in_fahrenheit)
