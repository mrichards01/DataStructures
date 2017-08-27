from counting_sort import CountingSort
from radix_sort import RadixSort
from heap_sort import HeapSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from bubble_sort import BubbleSort
from selection_sort import SelectionSort
from insertion_sort import InsertionSort
from time import time

import random

options = {
	1:("Bubble Sort", BubbleSort()),
	2:("Selection Sort", SelectionSort()),
	3:("Insertion Sort", InsertionSort()),
	4:("Quick Sort", QuickSort()),
	5:("Merge Sort", MergeSort()),
	6:("Radix Sort", RadixSort()),
	7:("Counting Sort", CountingSort()),
	8:("Heap Sort",HeapSort())
}
print ("Sorting Options: ")
for i in options.keys():
	print ("Option {} : {}".format(i, options[i][0]))
while True:
	option = int(input("Enter sorting option: "))
	sort_alg = options[option][1]
	start = time()
	arr = [random.randint(-100000,100000) for _ in range(10)]
	print (arr)
	sort_alg.sort(arr)
	end = time()
	print (arr)
	print ("Total Time (seconds): "+str(end-start))