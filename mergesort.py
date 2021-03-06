import random as r
from ttictoc import TicToc
import matplotlib.pyplot as plt 
t = TicToc()
run=0
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)


alist = [r.randint(500, 9000),r.randint(500, 9000),r.randint(500, 9000),r.randint(500, 9000),r.randint(500, 9000),r.randint(500, 9000)]
mergeSort(alist)
print(alist)
#print(random())
i =0
times = []
while i<10:
    t.tic()
    mergeSort([])
    t.toc()
    print('Time',i,":",t.elapsed)
    times.append(t.elapsed)
    i=i+1
#print(timeit.timeit(mergeSort([])))
print(times)
plt.plot([0,1000,2000,3000,4000,5000,6000,7000,8000,9000], times,marker='o',linewidth = 2) 
  
# naming the x axis 
plt.xlabel('Merge Number') 
# naming the y axis 
plt.ylabel('Time') 