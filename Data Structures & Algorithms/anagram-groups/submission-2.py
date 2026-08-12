class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, list[str]] = {}

        for c in range(len(strs)):
            key: str = "".join(sorted(strs[c]))
            if key in groups:
                groups[key].append(strs[c])
            else:
                groups[key] = [strs[c]]
        
        return list(groups.values())