class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_array=nums1+nums2
        merge_array.sort()
        if len(merge_array)%2==0:
            median=(merge_array[int((len(merge_array)/2)-1)] + merge_array[int(((len(merge_array)/2)+1)-1)])/2
        else:
            median=merge_array[int(((len(merge_array)+1)/2)-1)]
        return median