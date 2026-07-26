class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        product=1
        for i in range(3): 
            product=product * nums[i]
            i=+1
        return product