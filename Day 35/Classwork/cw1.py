#1. შექმენით ფუნქცია, რომელიც ითვლის სამკუთხედის პერიმეტრს (ყველა გვერდის ჯამს), სადც გექნებათ 3 არგუმენტი, სამიცე გვერდის სიგრძე.
def triangle_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

perimeter = triangle_perimeter(3, 4, 5)
print("სამკუთხედის პერიმეტრია:", perimeter)
