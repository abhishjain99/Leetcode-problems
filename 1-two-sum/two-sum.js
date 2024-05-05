/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var hash_map = new Map();
    var ans = [];
    for(var i = 0; i < nums.length; i++) {
        var complement = target - nums[i];
        if(hash_map.has(complement)) {
            return [hash_map.get(complement), i];
        }
        hash_map.set(nums[i], i);
    }
    return null;
};