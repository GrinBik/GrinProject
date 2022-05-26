import sys

n = int(input())

phone_book = {}

for i in range(n):
    line = input().split()
    phone_book[line[0]] = line[1]

lines = []

while True:
    try:
        line = input()
        if line in phone_book.keys():
            print(line + "=" + phone_book[line])
        else:
            print("Not found")
    except:
        break