class Solution:
    def maxSlidingWindow(self, nums, k):
        head = 0
        tail = 0
        max_num_list = []
        for i in range(len(nums)):
            if head - tail > k - 1:
                max_num_list.append(nums[head])

            queue = nums[head:tail]
            if nums[i] > nums[head] and i - head == k:
                head = i
            else:
                tail = i

        return max_num_list


if __name__ == "__main__":
    cls = Solution()
    cc = cls.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(cc)