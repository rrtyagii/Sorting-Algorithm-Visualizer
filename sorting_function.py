#import random
import time
#from GUI import draw_array
#from datetime import timedelta


class sorting_function:
    def bubble_sort(self,lst,draw_array, timetick):
        for _ in range(len(lst)-1):
            for j in range(len(lst)-1):
                if lst[j] > lst[j+1]:
                    lst[j],lst[j+1] = lst[j+1], lst[j]
                    draw_array(lst, ['#8351a1' if x == j or x==j+1 else '#6c9ff0' for x in range(len(lst))])
                    time.sleep(timetick)

    def insertion_sort(self, lst, draw_arra, timetick):
        for i in range(1, len(lst)):
            key = lst[i]
            j = i-1
            while j>=0 and lst[j] > key:
                lst[j+1] = lst[j]
                j-=1
            lst[j+1] = key
            draw_arra(lst, ['#8351a1' if x == j or x==j+1 else '#6c9ff0' for x in range(len(lst))] )
            time.sleep(timetick)

    def selection_sort(self, lst, draw_array, timetick):
        for i in range(len(lst)):
            min_index = i
            for j in range(i+1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j
            if min_index != i:
                lst[i], lst[min_index] = lst[min_index], lst[i]
                draw_array(lst,['#8351a1' if x == j or x==j+1 else '#6c9ff0' for x in range(len(lst))] )
                time.sleep(timetick)

    def merge_sort(self, lst, drawData, timeTick):
        if len(lst) <=1:
            return lst
        else:
            mid = len(lst)//2
            return self._merge(self.merge_sort(lst[mid:] , drawData, timeTick), self.merge_sort(lst[:mid], drawData, timeTick ) , drawData, timeTick)

    def _merge(self, lst1, lst2, drawData, timeTick):
        merge = []
        i=j=0
        while i<len(lst1) or  j<len(lst2):
            if j == len(lst2) or (i<len(lst1) and lst1[i] < lst2[j] ):
                merge.append(lst1[i])
                i+=1
            else:
                merge.append(lst2[j])
                j+=1
        return merge



    def quick_sort(self, arr, start, end, draw_array, timetick):
        if start >= end:
            return
        index = self._partition(arr, start, end, draw_array, timetick)
        self.quick_sort(arr, start, index-1, draw_array, timetick)
        self.quick_sort(arr, index+1, end, draw_array, timetick)

    def _partition(self, arr, start, end, draw_array, timetick):
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
                draw_array(arr,['#8351a1' if x == j or x==j+1 else '#6c9ff0' for x in range(len(lst))] )
                time.sleep(timetick)

            else:
                break
        arr[start], arr[high] = arr[high], arr[start]
        return high

    def colour_codes_mergeSort(self, length, left, middle, right):
        colour_codes =[]
        for i in range(length):
            if i>=left and i<=right:
                if i>=left and i<=middle:
                    colour_codes.append("#8351a1")
                else:
                    colour_codes.append("#f48cfc")
            else:
                colour_codes.append('#6c9ff0')
        return colour_codes



sorti = sorting_function()
lst = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(lst)
print("#Sorted List")
#start_time = time.process_time()

mergeSort=(sorti.merge_sort(lst))

#elapsed = (time.process_time() -start_time)
print(mergeSort)
