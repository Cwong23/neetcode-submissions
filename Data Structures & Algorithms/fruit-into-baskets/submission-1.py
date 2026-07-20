class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 1
        basket = {fruits[0]: 1} # stores the fruit id: amount of fruit

        left, right = 0, 1

        while left<right and right<len(fruits):
            if fruits[right] in basket:
                basket[fruits[right]]+=1
                res = max(res, right-left+1)
                right+=1
            else:
                if len(basket) < 2:
                    basket[fruits[right]] = 1
                    res = max(res, right-left)
                    right+=1
                else:
                    while True:
                        basket[fruits[left]]-=1
                        if basket[fruits[left]] == 0:
                            del basket[fruits[left]]
                            left+=1
                            basket[fruits[right]] = 1
                            res = max(res, right-left)
                            right+=1
                            break
                        left+=1                        

        return res