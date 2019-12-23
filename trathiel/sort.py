import time


f = open("testCaseRandom.txt", "r")
array=[]
for i in f:
    array.append(int(i))

start_time = time.time()


for i in range(len(array)):
    for j in range(len(array)-1,0,-1):
        if array[j-1] > array[j]:
            array[j-1],array[j] = array[j],array[j-1]

print(array)

print("--- %s seconds ---" % (time.time() - start_time))
