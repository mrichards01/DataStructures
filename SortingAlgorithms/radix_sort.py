from base_sort import BaseSort

class RadixSort(BaseSort):
	@staticmethod
	def count_sort(arr, exp):
		base = 10

		counts = [0] * base
		for curr in arr:
			counts[(curr//exp)%base]+=1

		# form prefix sum with the counts array
		for i in range(1, base):
			counts[i]+=counts[i-1]

		# use the counts array to get the given position of any number
		output = [None] * len(arr)
		start_pos = 0
		for i in range(len(arr)-1, -1, -1):
			pos = counts[(arr[i]//exp)%base]-1
			output[pos] = arr[i]
			counts[(arr[i]//exp)%base]-=1
		
		for i in range(len(arr)):
			arr[i] = output[i]

	@staticmethod
	def split_positive_and_negative(arr):
		negative = []
		positive = []
		for x in arr:
			if x<0:
				negative.append(abs(x))
			else:
				positive.append(x)

		return (positive, negative)

	# function is used to sort numbers of one polarity - either positive or negative numbers
	@staticmethod
	def sort_one_direction(arr, is_all_positive):
		# sort from least significant to most significant bit
		max_val = max(arr)

		exp = 1
		while max_val//exp>0:
			# sort current unit
			RadixSort.count_sort(arr, exp)
			exp *= 10

		if is_all_positive:
			return

		# reverse array if negative numbers were sorted
		i = 0 
		j = len(arr)-1
		while i<=j:
			arr[i], arr[j] = -arr[j], -arr[i]
			i+=1
			j-=1

	def sort(self, arr):
		nums = RadixSort.split_positive_and_negative(arr)
		RadixSort.sort_one_direction(nums[0], True)
		RadixSort.sort_one_direction(nums[1], False)

		# replace array with all numbers in the first negative array and then the positive array
		for i in range(len(nums[1])):
			arr[i] = nums[1][i]
		
		no_of_positive_nums = len(nums[1])
		for i in range(len(nums[0])):
			arr[i+no_of_positive_nums] = nums[0][i]
