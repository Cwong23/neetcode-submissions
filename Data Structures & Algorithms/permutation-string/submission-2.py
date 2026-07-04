class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False
        
        counts_1 = [0] * 26
        counts_2 = [0] * 26

        for i in range(s1_len):
            counts_1[ord(s1[i]) - 97]+=1
            counts_2[ord(s2[i]) - 97]+=1

        for i in range(s1_len, s2_len):
            if counts_1 == counts_2:
                return True
            counts_2[ord(s2[i]) - 97]+=1
            counts_2[ord(s2[i - s1_len]) - 97]-=1
        
        if counts_1 == counts_2:
                return True

        return False