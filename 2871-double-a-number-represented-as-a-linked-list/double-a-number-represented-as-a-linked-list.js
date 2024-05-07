/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var doubleIt = function(head) {
    var dummy = curr = head;
    var carry = new ListNode();
    while(curr != null) {
        curr = curr.next;
        c_val = curr !== null ? curr.val : 0
        summ = dummy.val * 2 + Math.floor((c_val * 2) / 10)
        dummy.val = summ % 10
        if(summ > 9 && dummy == head) {
            carry.val = Math.floor(summ / 10)
            carry.next = head
            head = carry
        }
        dummy = dummy.next
    }
    return head
};