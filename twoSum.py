 def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        f = []
        t1 = 0
        t2 = 0
        l2 = [target - num for num in nums]
        for i in range(len(nums)):
            temp = l2[i]
            l2[i] = None
            if nums[i] in l2:
                t1 = l2.index(nums[i])
                t2 = nums.index(nums[i])
                l2[i] = temp
                break
            l2[i] = temp
        f.append(t2)
        f.append(t1)
        return f