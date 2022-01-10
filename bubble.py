import time


def bubbleSort(test):
    n = len(test)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if test[j] > test[j + 1] :
                test[j], test[j + 1] = test[j + 1], test[j]
 

test = [100,10,11,12,130,300,2000,9,94]
time_start = time.time()
bubbleSort(test)
time.sleep(1)           

print ("Sorted array is:")
for i in range(len(test)):
    print ("% d" % test[i],end="")

time_end = time.time()
print("\n"f'sorting took {time_end-time_start} seconds') 
