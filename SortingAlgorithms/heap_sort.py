from base_sort import BaseSort
import math

class HeapSort(BaseSort):
	def __build_heap(self, arr):
		self.__heap = [] # heap starting from 1 for easiness
		self.__heap.append(None)
		for x in arr:
			self.__heap.append(x)
		self.__size = len(self.__heap)

		# heapify only n/2 elements need to be heapified
		for i in range(math.ceil(len(self.__heap)//2),0,-1):
			self.__heapify_down(i)

	def __swap(self, idxA, idxB):
		self.__heap[idxA], self.__heap[idxB] = self.__heap[idxB], self.__heap[idxA]

	def __extract_min(self):
		# swap root with the end of the heap and heapify down
		root = self.__heap[1]
		self.__swap(1, self.__size-1)
		self.__heap[self.__size-1] = None
		self.__size-=1

		self.__heapify_down(1)
		return root

	def __heapify_down(self, idx):
		leftIdx = idx*2
		rightIdx = idx*2+1

		lowest_idx = idx
		if leftIdx<self.__size and self.__heap[leftIdx]<self.__heap[lowest_idx]:
			lowest_idx = leftIdx

		if rightIdx<self.__size and self.__heap[rightIdx]<self.__heap[lowest_idx]:
			lowest_idx = rightIdx

		if lowest_idx!=idx:
			self.__swap(lowest_idx, idx)
			self.__heapify_down(lowest_idx)

	def sort(self, arr):
		# initialise heap
		self.__build_heap(arr)
		output = []
		while self.__size>1:
			x = self.__extract_min()
			output.append(x)

		for i in range(len(output)):
			arr[i] = output[i]