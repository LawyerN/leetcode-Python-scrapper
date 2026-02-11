if i >= 0 and nums1[i] > nums2[j]:
    nums1[right] = nums1[i]
    i -= 1
else:
    nums1[right] = nums2[j]
    j -= 1