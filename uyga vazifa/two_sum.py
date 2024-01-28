nums=[int(input())for i in range(5)]
target=int(input())
nums2 = sorted(nums)
for i in range(len(nums2) - 1):
    t1 = i+1
    t2 = len(nums2) - 1
    while(t1 <= t2):
        t = int((t1 + t2)/2)
        if nums2[i] + nums2[t] == target:
            i1 = nums.index(nums2[i])
            i2 = nums.index(nums2[t])
            if i1 == i2:
                i2 = 1 + i1 + nums[i1+1:].index(nums2[t])
                print( [i1, i2])
        elif nums2[i] + nums2[t] > target:
            t2 = t - 1
        else:
            t1 = t+1