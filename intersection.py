def intersection(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))                                  