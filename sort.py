class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        return a list that contains the merged array
        """


nums1 = [1,2,3]
m = 3
nums2 = [2,5,6]
n = 3

s = Solution()
print(s.merge(nums1, m, nums2, n))

# EXPECTED OUTPUT:
# [1,2,2,3,5,6]