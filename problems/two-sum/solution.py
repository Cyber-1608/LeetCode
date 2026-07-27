class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i,num in enumerate(nums):
            comple=target-num
            if comple in visited:return [visited[comple],i]
            visited[num]=i