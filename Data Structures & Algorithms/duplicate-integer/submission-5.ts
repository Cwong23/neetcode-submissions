class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const duplicates = new Map<number, number>;

        for (const num of nums){
            if (duplicates.has(num)) {
                return true;
            }
            duplicates.set(num, num);
        }

        return false;
    }
}
