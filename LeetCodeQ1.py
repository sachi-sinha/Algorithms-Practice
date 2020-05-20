class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ''' Brute Force'''
        sol = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    sol.append(i)
                    sol.append(j)
                    break
        return sol
        
        '''Two pass Hash Table'''
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if (indices.has_key(complement) and indices.get(complement) != i):
                return [i,indices.get(complement)]
                
        '''One pass Hash Table'''
        indices = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if (indices.has_key(complement)):
                return [i, indices.get(complement)]
            indices[nums[i]] = i
