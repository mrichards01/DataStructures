from base_sort import BaseSort

class QuickSort(BaseSort):

	@staticmethod
	def partition(start, end, arr):
		# let the pivot be the first element
		pivot_idx = start
		pivot_val = arr[pivot_idx]
		i = start
		j = end
		while i<=j:
			# shift left pointer until element larger than the pivot found
			while arr[i]<pivot_val and i<end:
				i+=1
			# shift right pointer until element smaller than the pivot found
			while arr[j]>pivot_val and j>0:
				j-=1

			# swap elements where left and right pointer have not reached each other
			if i<=j:
				arr[j], arr[i] = arr[i], arr[j]
				i+=1
				j-=1

		return i
		
	def sort(self, arr):
		QuickSort.sort_range(0, len(arr)-1, arr)

	@staticmethod
	def sort_range(start, end, arr):
		if start<end:
			pivot_idx = QuickSort.partition(start, end, arr)
			if start<pivot_idx-1:
				QuickSort.sort_range(start, pivot_idx-1, arr)
			if pivot_idx<end:
				QuickSort.sort_range(pivot_idx, end, arr)

