class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []

        nums_length = len(nums)

        nums_copy = nums.copy()
        nums_copy.sort()

        for i in range(0, nums_length-2):
            if 0 < i and nums_copy[i] == nums_copy[i-1]:
                continue
            j = i+1
            k = nums_length-1
            
            while True:
                val = nums_copy[i] + nums_copy[j] + nums_copy[k]

                if val < 0 :
                    j += 1
                    while nums_copy[j] == nums_copy[j-1] and j < k:
                        j += 1
                elif val == 0 :
                    answer.append([nums_copy[i],nums_copy[j],nums_copy[k]])
                    j += 1
                    while nums_copy[j] == nums_copy[j-1] and j < k:
                        j += 1
                else:
                    k -= 1
                    
                if j == k:
                    break

        return answer