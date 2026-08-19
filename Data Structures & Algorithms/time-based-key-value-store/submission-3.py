class TimeMap:

    def __init__(self):
        self.mem = {}
        self.mem_times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mem:
            self.mem[key] = {}
            self.mem_times[key] = []
        self.mem[key][timestamp] = value
        self.mem_times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mem:
            return ""
        if timestamp not in self.mem[key]:
            arr = self.mem_times[key]
            res = ""
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= timestamp:
                    res = self.mem[key][arr[mid]]
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        else:
            return self.mem[key][timestamp]