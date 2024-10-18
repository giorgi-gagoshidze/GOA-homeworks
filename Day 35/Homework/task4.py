#4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).
def list_of_lengths(strings):
    return [len(s) for s in strings]
result = list_of_lengths(["გამარჯობა", "სალამი", "hello"])
print(result)