class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # have set to track the characters
        # have window that grows with more unique characters
        # keep track of max size 
        # when char is duplicate, continously remove from set and shrink window
        # until that char is no longer in the set
        # if left + 1 == right and it is not a unique characer, shift entire window

        if not s:
            return 0

        uniques = {s[0]}
        max_size = 1

        left, right = 0, 1

        while right < len(s):
            curr = s[right]
            if curr not in uniques:
                uniques.add(curr)
                right+=1
                max_size = max(max_size, right - left)
            else:
                if left + 1 == right:
                    right+=1
                else:
                    uniques.remove(s[left])
                left += 1
        return max_size