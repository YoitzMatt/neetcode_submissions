/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // if n = len of the list 
        // remove the head of the list
        // get the length of the list
        // then utilize pre and curr ptrs to remove the node
        int len{};
        ListNode* count = head;
        while (count != nullptr) {
            len++;
            count = count->next;
        }

        int targetidx = len - n;
        if (targetidx == 0)
            return head->next;
        int i{};
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (head != nullptr) {
            if (i == targetidx) {
                ListNode* tmp = curr->next;
                prev->next = tmp;
                curr->next = nullptr;
                break;
            } 
            i++;
            prev = curr;
            curr = curr->next;
            
        }
        return head;
    }
};
