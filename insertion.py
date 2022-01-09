import time

def insertionSort(test):
  
    for i in range(1, len(test)):  
        key = test[i]
        j = i-1
        while j >=0 and key < test[j] :
                test[j+1] = test[j]
                j -= 1
        test[j+1] = key
  
 
test = [100,10,11,12,130,300,2000,9,94]
time_start = time.time()
insertionSort(test)
n = len(test)
time.sleep(1)           


print ("Sorted array is:")
for i in range(len(test)):
    print ("%d" %test[i], end = " ")


time_end = time.time()
print("\n"f'sorting took {time_end-time_start} seconds') 
