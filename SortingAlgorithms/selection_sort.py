from base_sort import BaseSort

class SelectionSort(BaseSort):
	def sort(self, arr):
		for i in range(len(arr)):
			smallest = i
			for j in range(i+1, len(arr)):
				if arr[j]<arr[smallest]:
					smallest = j

			arr[i], arr[smallest] = arr[smallest], arr[i]