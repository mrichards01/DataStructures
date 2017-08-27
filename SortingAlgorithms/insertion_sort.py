from base_sort import BaseSort

class InsertionSort(BaseSort):
	def sort(self, arr):
		for i in range(1, len(arr)):
			to_insert = arr[i]
			# shift all elements to the right until the correct insertion point is found
			j = i-1
			while j>=0 and to_insert<arr[j]:
				arr[j+1] = arr[j]
				j-=1

			arr[j+1] = to_insert