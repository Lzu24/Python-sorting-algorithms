import time

test = [100,10,11,12,130,300,2000,9,94]

for i in range(len(test)):
    for j in range(i+1, len(test)):
        if test[min_idx] > test[j]:
            min_idx = j
                      
    test[i], test[min_idx] = test[min_idx], test[i]
  
time_start = time.time()
time.sleep(1)           

print ("Sorted array")
for i in range(len(test)):
    print("%d" %test[i],end = ", ")

time_end = time.time()
print("\n"f'sorting took {time_end-time_start} seconds') 
