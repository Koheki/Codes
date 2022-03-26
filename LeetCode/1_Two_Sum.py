class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums = [int(n) for n in input()[1:-1].split(",")]
        # target = int(input())

        D = {}

        for i in range(len(nums)):
            n = target - nums[i]
            if  n not in D:
                D[n] = [i]
            else:
                tmp = D[n]
                tmp.append(i)
                D[n] = tmp


        for i in range(len(nums)):
            if nums[i] in D:
                # print(nums[i],D)

                if len(D[nums[i]]) == 2:
                    return D[nums[i]]

                else:
                    if D[nums[i]][0] != i:
                        D[nums[i]].append(i)
                        return D[nums[i]]

