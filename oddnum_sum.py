n = str(input("Enter the integer input:"))
odd_value = 0
for i in n:
    if int(i) % 2 == 1:
        odd_value += int(i)
print(odd_value)
