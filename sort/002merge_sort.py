import random

class Solution(object):
	def merge_sort(self, nums, p, r):
		q = (p+r)/2
		if p<r:
			self.merge_sort(nums, p, q)
			self.merge_sort(nums, q+1, r)
		return self.merge(nums, p, q, r)

	def merge(self, nums, p, q, r):
		L = []
		R = []
		for i in range(p, q+1):
			L.append(nums[i])
		for j in range(q+1,r+1):
			R.append(nums[j])
		L.append(float("inf"))
		R.append(float("inf"))
		i = 0
		j = 0
		for k in range(p,r+1):
			if L[i] <R[j]:
				nums[k] = L[i]
				i +=1
			else:
				nums[k] = R[j]
				j +=1

		return nums

def main():
	A = []
	for i in range(4):
		A.append(random.randint(0,100))
	print "the original A is:", A
	nums = Solution().merge_sort(A,0,len(A)-1)
	print "the merge_sorted is:", nums

if __name__ == '__main__':
	main()