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

#     def merge_sort(self, lst, drawData, timeTick):
# #        print(lst)
#         if len(lst) <=1:
#             return lst
#         else:
#             mid = len(lst)//2
#             firstHalf= self.merge_sort(lst[mid:])
#             secondHalf = self.merge_sort(lst[:mid])
#             result = self._merge(firstHalf, secondHalf, drawData, timeTick)
# #            print(result)
#             return result
#
#     def _merge(self, lst1, lst2, drawData, timeTick):
#
#         merge = []
#
#         i=j=0
#         while i<len(lst1) or  j<len(lst2):
#             if j == len(lst2) or (i<len(lst1) and lst1[i] < lst2[j] ):
#                 merge.append(lst1[i])
#                 i+=1
#             else:
#                 merge.append(lst2[j])
#                 j+=1
#         return merge
    def merge_sort(self, lst, drawData, timeTick):
        self._merge_sort(lst, 0, len(lst)-1, drawData, timeTick)

    def _merge_sort(self, lst, left, right, drawData, timeTick):
        if left<right:
            mid = (left+right)//2
            self._merge_sort(lst, left, mid, drawData, timeTick )
            self._merge_sort(lst, mid+1, right, drawData, timeTick )
            self._merge(lst, left, mid, right, drawData, timeTick)

    def _merge(self, lst, left, midpoint, right, drawData, tickTime):
        drawData(lst, self.colour_codes_mergeSort(len(lst), left, midpoint, right))
        time.sleep(tickTime)

        L = lst[left:midpoint+1]
        R = lst[midpoint+1:right+1]

        i=j=0

        for idx in range(left, right+1):
            if i< len(L) and j< len(R):
                if L[i] < R[j]:
                    lst[idx] = L[i]
                    i+=1
                else:
                    lst[idx] = R[j]
                    j+=1
            elif i< len(L):
                lst[idx] = L[i]
                i+=1
            else:
                lst[idx] = R[j]
                j+=1
        drawData(lst, ['#8351a1' if x >= left or x <=right else '#6c9ff0' for x in range(len(lst))] )
        time.sleep(tickTime)

    def quick_sort(self, arr, start, end): #, draw_array, timetick):
        if start <end:
            index = self._partition(arr, start, end)#, draw_array, timetick)
            self.quick_sort(arr, start, index-1)#, draw_array, timetick)
            self.quick_sort(arr, index+1, end)#, draw_array, timetick)

    def _partition(self, arr, start, end):#, draw_array, timetick):
        i = start - 1
        pivot = arr[end]

        for j in range(start, end):
            if arr[j] < pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[end] = arr[end], arr[i+1]
        return (i+1)
#         high  = end
#         while True:
#             while low<=high and arr[high] >= pivot:
#                 high = high -1
#             while low<= high and arr[low] <= pivot:
#                 low = low + 1
#             if low<= high:
#                 arr[low], arr[high] =arr[high], arr[low]
# #                draw_array(arr,['#8351a1' if x == j or x==j+1 else '#6c9ff0' for x in range(len(lst))] )
# #                time.sleep(timetick)
#             else:
#                 break
#         arr[start], arr[low] = arr[low], arr[low]
#         return low

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


    def _colour_for_quicksort(self, length, left, right, partition, currIdx, swapped=false):
        colourArray = []
        for i in range(length):
            if i<= left and i:
                pass


sorti = sorting_function()
lst = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(lst)
print("#Sorted List")
#start_time = time.process_time()

(sorti.quick_sort(lst, 0, len(lst)-1))
print(lst)
#elapsed = (time.process_time() -start_time)
#print(mergeSort)
