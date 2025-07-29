from problem2 import move_zeroes

def test():
    nums1 = [0, 1, 0, 3, 12]
    move_zeroes(nums1)
    print(nums1)  # [1, 3, 12, 0, 0]
    nums2 = [1, 2, 3, 4]
    move_zeroes(nums2)
    print(nums2)  # [1, 2, 3, 4]
    nums3 = [0, 0, 0, 0]
    move_zeroes(nums3)
    print(nums3)  # [0, 0, 0, 0]

test()