class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        var l = 0;
        var r = numbers.length - 1;
        while (l < r){
            const curr = numbers[l] + numbers[r];
            if (curr == target){
                return [l + 1, r + 1];
            } else if (curr < target){
                l++;
            } else {
                r--;
            }
        }
        return [-1, -1];
    }
}
