class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False
        
        ptr1, ptr2, tot = 0, 0, s1_len
        curr = {}
        for c in s1:
            curr[c] = curr.get(c, 0) + 1
        
        while ptr2 < s2_len:
            if ptr2 - ptr1 > s1_len - 1:
                if s2[ptr1] in curr:
                    curr[s2[ptr1]] += 1
                    tot += 1 if curr[s2[ptr1]] > 0 else 0
                ptr1+=1
            if s2[ptr2] in curr:
                curr[s2[ptr2]] -= 1
                tot -= 1 if curr[s2[ptr2]] >= 0 else 0

            if tot == 0:
                return True
            
            
            ptr2 += 1
        return False