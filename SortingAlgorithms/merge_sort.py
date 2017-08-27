from base_sort import BaseSort

class MergeSort(BaseSort):

	@staticmethod
	def merge(arr, left, mid, right):
		new_arr = []

		# fill temporary left and right arrays
		left_arr = []
		for i in range(0, mid-left+1):
			left_arr.append(arr[left+i])

		right_arr = []
		for i in range(0, right-mid):
			right_arr.append(arr[mid+1+i])

		i = 0
		j = 0
		curr_pos = left 
		while i<len(left_arr) and j<len(right_arr):
			# use the smallest element to fill the general array until left or right arrays have no elements remaining
			if left_arr[i]<=right_arr[j]:
				arr[curr_pos] = left_arr[i]
				i+=1
			else:
				arr[curr_pos] = right_arr[j]
				j+=1
			curr_pos+=1

		# insert remaining elements from left array
		while i<len(left_arr):
			arr[curr_pos] = left_arr[i]
			i+=1
			curr_pos+=1

		# insert remaining elements from right array
		while j<len(right_arr):
			arr[curr_pos] = right_arr[j]
			j+=1
			curr_pos+=1

	def sort(self, arr):
		MergeSort.sort_range(arr, 0, len(arr)-1)

	@staticmethod
	def sort_range(arr, start, end):
		# recursively sort until only one element is remaining
		if start<end:
			mid = (start+end)//2
			MergeSort.sort_range(arr, start, mid)
			MergeSort.sort_range(arr, mid+1, end)
			MergeSort.merge(arr, start, mid, end)
		return arr

