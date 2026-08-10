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
    bool hasCycle(ListNode* head) {
        std::unordered_map<ListNode*, bool> visited;
        while (head != nullptr) {
            if (!visited.count(head)) {
                visited[head] = true;
            } else {
                return true;
            }

            head = head->next;
        }

        return false;
    }
};
