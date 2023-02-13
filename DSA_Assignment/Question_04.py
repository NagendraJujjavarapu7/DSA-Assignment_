def Palindrome(s):
    return word == word[::-1]
word = "EVE"
ans = Palindrome(word)
if ans:
    print("Yes")
else:
    print("No")