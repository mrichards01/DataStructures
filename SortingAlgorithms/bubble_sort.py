from base_sort import BaseSort

class BubbleSort(BaseSort):
	def sort(self, arr):
		for k in range(0,len(arr)-1):
			used_swaps = False
			for i in range(1, len(arr)-k):
				if arr[i]<arr[i-1]:
					arr[i], arr[i-1] = arr[i-1], arr[i]
					used_swaps = True

			if not used_swaps:
				return