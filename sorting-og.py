N = int(input("How many values do you want to enter: "))
N2 = N

if(0 < N2 <= 1000):
    numbers = list()
    while True:
        if(N == 0):
            break
        else:
            numbers.append(int(input("Enter the Value-" + str(N) + ": ")))
            N = N-1

    for a in range(0, len(numbers)):
        for i in range(a+1, len(numbers)):
             if (i+1) != len(numbers) and numbers[a] < numbers[(i)]:
                c = numbers[a]
                numbers[a] = numbers[i]
                numbers[i] = c

    numbers.sort(reverse=True)
    e = "Output: "
    while (0 < N2):
        if(N2 == 1):
            e += str(numbers[N2 - 1])
        else:
            e += str(numbers[N2 - 1]) + "-"
        N2 = N2 - 1
else:
   e = "Please enter the value between 0 and 1000 !"
print(e)
while(True):
    if(input()):
        break