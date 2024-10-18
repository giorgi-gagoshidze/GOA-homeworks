#5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.
def is_palindrome(s):
    return s == s[::-1]
result1 = is_palindrome("wow")
result2 = is_palindrome("hello")
print(result1)
print(result2)