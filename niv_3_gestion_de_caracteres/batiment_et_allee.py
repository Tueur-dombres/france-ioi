import sys
input = sys.stdin.readline

nom  = input()
age = int(input())
print(ord(nom[0].lower()) - ord("a") + 1, end ="")
print(chr(age + ord("a") - 1).upper())