# -*- coding: utf-8 -*-
import random  as r

from ttictoc import TicToc
import matplotlib.pyplot as plt 
t = TicToc()
run=0
def mergeSort(alist):
   global run
   run= 1+run
   f = run/17
   print("IS INTEGER",f.is_integer())
   print(run)
   if f.is_integer() or run==1:   
      alist = [r.randint(501,10000 ),r.randint(501,10000 ),r.randint(501,10000 ),r.randint(501,10000 ),r.randint(501,10000 ),r.randint(501,10000 ),r.randint(501,10000 ),r.randint(501,10000 ),r.randint(501,10000 )]
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
plt.plot([1,2,3,4,5,6,7,8,9,10], times,marker='o',linewidth = 2) 
  
# naming the x axis 
plt.xlabel('Merge Number') 
# naming the y axis 
plt.ylabel('Time') 
  