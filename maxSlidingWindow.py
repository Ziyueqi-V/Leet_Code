class Solution:
    def maxSlidingWindow(self, nums, k):
        max_nums = []

        def pick_max_num(nums_list, w):  # w为窗口宽度，即临时数组的长度
            max_num = nums_list[0]  # 窗口内的最大数默认为第一个
            for j in range(w):
                if nums_list[j] > max_num:
                    max_num = nums_list[j]
            return max_num

        for i in range(len(nums) - k + 1):
            max_nums.append(pick_max_num(nums[i:i + k], k))

        return max_nums


