from base_sort import BaseSort

class CountingSort(BaseSort):

	def sort(self, arr):
		# find the min and max values to use for the counts array
		min_val = 0
		max_val = 0
		for curr in arr:
			min_val = min(min_val, curr)
			max_val = max(max_val, curr)

		counts_size = max_val - min_val +1
		counts = [0] * counts_size

		for curr in arr:
			counts[curr-min_val]+=1

		# form prefix sum with the counts array
		for i in range(1, counts_size):
			counts[i]+=counts[i-1]

		# use the counts array to get the given position of any number
		output = [None] * len(arr)
		for i in range(len(arr)):
			pos = counts[arr[i]-min_val]-1
			output[pos] = arr[i]
			counts[arr[i]-min_val]-=1

		for i in range(len(arr)):
			arr[i] = output[i]
