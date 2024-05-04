/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    people.sort((a, b) => a - b);
    var left = 0;
    var right = people.length - 1;
    var boats = 0;
    while(left <= right) {
        if(people[left] + people[right] <= limit) {
            left += 1;
        }
        right -= 1;
        boats += 1;
    }
    return boats;
};