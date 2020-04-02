N = int(input("Please enter yon need number:"))
sum = 0
count = 0
print("please input {} number:".format(N))
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum / N
print(" N = {},sum = {}".format(N,sum))
print("Average = {:.2f}".format(average))
