def isPalindrome(x):
    if x < 0:
        print("False")
        return False
    s = str(x)
    if  s == s[::-1]:
        print("True")
        return True
    else:
        print("False")
        return False
num = int(input("Enter a number:"))
isPalindrome(x=num)