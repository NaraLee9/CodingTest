nums1 = [3,1,2,3]
nums2 = [3,3,3,2,2,4]
nums3 = [3,3,3,2,2,2]

def solution(nums):
    limit = len(nums)
    types = set(nums)

    return min(len(types), limit)

solution(nums1)
solution(nums2)
solution(nums3)