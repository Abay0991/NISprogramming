#Comments on the codes

max_value = int(input("Please enter a maximum value: "))
current = 1

while current <= max_value:
    total = 0

    for i in range(1, current):
        if current % 1 == 0:
            total += 1

    if total == current:
        print(current, end=" ")

    current += 1

