import math
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        len1 = len(nums1)
        len2 = len(nums2)
        newLen = len1 + len2
        nums3 = []
        i = 0
        j = 0

        while(i < len1 or j < len2):

            if i >= len1:
                nums1.append(float("inf"))
            elif j >= len2:
                nums2.append(float("inf"))

            if(nums1[i] < nums2[j]):
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1


        if newLen % 2 == 0:
            return (nums3[(newLen // 2)] + nums3[(newLen // 2) - 1]) / 2
        else:
            return nums3[newLen // 2]

nums1 = [1, 2]
nums2 = [3]

print(Solution.findMedianSortedArrays(Solution, nums1, nums2))