num = int(input())
while num < 0 or num > 100:
    num = int(input())
allnum = num
b = []
x = []
total = 0
while num != 0:
    b.append(num % 10)
    num //= 10
    total += 1
counter = 0
for i in range(len(b)):
    if total == 3:
        x.append("C")
        break
    counter += 1
    if counter == 1:
        if b[i] == 0:
            break
        if b[i] <= 3:
            x.append("I" * (b[i]))
        if b[i] == 4:
            x.append("IV")
        if b[i] > 4 and b[i] <= 8:
            x.append("V" + "I" * (b[i] - 5))
        if b[i] == 9:
            x.append("IX")
    if counter == 2:
        if b[i] == 0:
            break
        if b[i] <= 3:
            x.append("X" * (b[i]))
        if b[i] == 4:
            x.append("XL")
        if b[i] > 4 and b[i] <= 8:
            x.append("L" + "X" * (b[i] - 5))
        if b[i] == 9:
            x.append("XC")
x = x[::-1]
print("".join(x))
