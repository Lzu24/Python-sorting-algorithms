import time  



def partition(test, low, high):
    i = (low-1)       
    pivot = test[high]    
  
    for j in range(low, high):
        if test[j] <= pivot:
            i = i+1
            test[i], test[j] = test[j], test[i]
  
    test[i+1], test[high] = test[high], test[i+1]
    return (i+1)


  
def quickSort(test, low, high):
    if len(test) == 1:
        return test
    if low < high:
        pi = partition(test, low, high)
  
        quickSort(test, low, pi-1)
        quickSort(test, pi+1, high)
  
  
test = [100,10,11,12,130,300,2000,9,94]
n = len(test)

time_start = time.time()
time.sleep(1)           

quickSort(test, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % test[i],end = " ")

time_end = time.time()
print("\n"f'sorting took {time_end-time_start} seconds') 
