/**
 * @param {number[]} happiness
 * @param {number} k
 * @return {number}
 */
var maximumHappinessSum = function(happiness, k) {
    happiness.sort((a, b) => (a > b ? -1 : 1));
    let ans = 0;
    let decrement = 0;

    for(let h = 0; h < k; h++) {
        let summ = happiness[h] - decrement++;
        if(summ < 0) summ = 0;
        ans += summ;
    }
    return ans;
};