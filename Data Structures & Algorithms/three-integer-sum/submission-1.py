class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create hash with numbers to indicies
        # 2 loop solution
        # two pointers
        # first pointer points to left most element, 2nd pointer goes from one to
        # the right to the end
        # move the 1st pointer to the right one, repeat
        # sum numbers, see if the negative number exists in the hash
        # this should guarantee that each list is unique
        # only accept numpers from hash where it is greater than the current index of the 2nd number

        if len(nums) < 3:
            return []

        # create hash
        reference: dict[int, list[int]] = {}
        nums.sort()

        for i, x in enumerate(nums):
            if x in reference:
                reference[x].append(i)
            else:
                reference[x] = [i]

        answer = []
        print(reference)
        visited = set()

        # loops
        for p1 in range(len(nums) - 2):
            x = nums[p1]
            if x in visited:
                continue
            else:
                visited.add(x)
            visited_y = set()
            for p2 in range(p1 + 1, len(nums)-1):
                y = nums[p2]
                if y in visited_y:
                    continue
                else:
                    visited_y.add(y)
                current = (x + y) * -1

                if current in reference:
                    # reference[current] gives us a list
                    # enumerate through the list
                    # check for the smallest possible value that is greater than p2
                    possible_nums: list[int] = reference[current]

                    i = 0
                    while i < len(possible_nums):
                        if p2 < possible_nums[i]:
                            answer.append([x, y, current])
                            break
                        i+=1
        return answer