import time

def mergeSort(nlist):
    
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1


nlist = [100,10,11,12,130,300,2000,9,94]
print (f'unsorted list is {nlist}\n')

time_start = time.time()
time.sleep(1)           

mergeSort(nlist)
print(f'list after mergesort is {nlist}')

time_end = time.time()
print("\n"f'sorting took {time_end-time_start} seconds') 
