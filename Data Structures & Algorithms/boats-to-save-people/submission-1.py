class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        # two pointers one starts at beg and other other is at end
        # see if that combination fits, if not add two boats
        l, r = 0, len(people) - 1
        print(people)
        while l<=r:
            if people[l] + people[r] <= limit:
                l+=1
            boats+=1
            r-=1            

        return boats