class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        cnt = []
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                cnt.append(True)
            else:
                cnt.append(False)

        res = []
        for q in queries:
            temp = 0
            for i in range(q[0], q[1]+1):
                if cnt[i]:
                    temp+=1
            res.append(temp)

        return res
