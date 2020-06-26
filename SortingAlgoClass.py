import random
import time
from datetime import timedelta


class Sorting:
    def bubble_sort(self,lst):
        for i in range(len(lst)):
            swapped= False
            for j in range(0, len(lst)-i-1):
                if lst[j]> lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    swapped = True
            if swapped == False:
                break
        return lst

    def insertion_sort(self, lst):
        for i in range(1, len(lst)):
            key = lst[i]
            j = i-1
            while j>=0 and lst[j] > key:
                lst[j+1] = lst[j]
                j-=1
            lst[j+1] = key
        return lst

    def selection_sort(self, lst):
        for i in range(len(lst)):
            min_index = i
            for j in range(i+1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j
            if min_index != i:
                lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst


    def merge_sort(self, lst):
        if len(lst)>1:
            mid= len(lst)//2
            L = lst[:mid]
            R = lst[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i=j=k=0
            while i < len(L) and j<len(R):
                if L[i] < R[j]:
                    lst[k] = L[i]
                    i+=1
                else:
                    lst[k] = R[j]
                    j+=1
                k+=1

            while i<len(L):
                lst[k] = L[i]
                i+=1
                k+=1

            while j<len(R):
                lst[k] = R[j]
                j+=1
                k+=1



    def quick_sort(self, arr, start, end):
        if start >= end:
            return
        index = self._partition(arr, start,end)
        self.quick_sort(arr, start, index-1)
        self.quick_sort(arr, index+1, end)

    def _partition(self, arr, start, end):
        low = start+1
        pivot = arr[start]
        high  = end
        while True:
            while low<=high and arr[high] >= pivot:
                high = high -1
            while low<= high and arr[low] <= pivot:
                low = low + 1
            if low<= high:
                arr[low], arr[high] =arr[high], arr[low]
            else:
                break
        arr[start], arr[high] = arr[high], arr[start]
        return high



sorti = Sorting()
lst = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(lst)
print("#Sorted List")
#start_time = time.process_time()

(sorti.merge_sort(lst))

#elapsed = (time.process_time() -start_time)

print(lst)