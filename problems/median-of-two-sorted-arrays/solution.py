class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum=0
        merge_arr=nums1+nums2
        for i in range(len(merge_arr)):
            sum=sum+merge_arr[i]
            i=+1
        median=sum/len(merge_arr)
        return median
