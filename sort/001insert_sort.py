class Solution(object):
    def insert_sort(self,nums):
        A = nums
        
        for i in range(1,len(nums)):
            key = A[i]
            j = i - 1
            
            while j>=0 and A[j] > key:
                A[j+1] = A[j]
                j -=1
            
            A[j+1] = key
        return A

def main():
    nums = insert_sort([5,2,3,1,6,4])
    print nums

if __name__ == "__main__":
    main()
