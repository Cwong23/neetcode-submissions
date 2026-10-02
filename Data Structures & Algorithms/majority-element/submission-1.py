class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        max_element = nums[0]
        for i in range(1, len(nums)):
            print(max_element)
            print(counter)
            if max_element == nums[i]:
                counter+=1
            else:
                if counter == 0:
                    max_element = nums[i]
                else:
                    counter-=1
        return max_element