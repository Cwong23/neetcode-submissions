class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Structure
        #    frequency: num
        freq: dict[int, int] = defaultdict(int)

        for t in range(len(nums)):
            key: int = nums[t]
            freq[key] += 1

        output: list[int] = []
        while k > 0:
            biggest: tuple[int, int] = max(freq.items(), key=lambda kv:kv[1])
            output.append(biggest[0])
            freq.pop(biggest[0])
            k-=1

        return output
