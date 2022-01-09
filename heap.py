import time

def heapify(test, n, i):
    largest = i  
    left = 2 * i + 1    
    right = 2 * i + 2    

    if left < n and test[i] < test[left]:
        largest = left
  
    if right < n and test[largest] < test[right]:
        largest = right
  
    if largest != i:
        test[i],test[largest] = test[largest],test[i] 
  
 
        heapify(test, n, largest)
  

def heapSort(test):
    n = len(test)
  
    for i in range(n // 2 - 1, -1, -1):
        heapify(test, n, i)
   
    for i in range(n-1, 0, -1):
        test[i], test[0] = test[0], test[i] 
        heapify(test, i, 0)
  
test = [100,10,11,12,130,300,2000,9,94]
time_start = time.time()
heapSort(test)
n = len(test)
time.sleep(1)           

print ("Sorted array is")
for i in range(n):
    print ("%d" %test[i],end=" ")

time_end = time.time()
print("\n"f'sorting took {time_end-time_start} seconds') 
