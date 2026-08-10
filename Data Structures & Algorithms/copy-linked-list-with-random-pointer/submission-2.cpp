/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        // Initalize a map
        // Iterate through the list mapping the current node to it's copy

        unordered_map<Node*, Node*> copies;
        copies[nullptr] = nullptr;
        Node* curr = head;
        while (curr != nullptr) {
            Node* nn = new Node(curr->val);
            copies[curr] = nn;
            curr = curr->next;
        }

        curr = head;
        while (curr != nullptr) {
            Node* cpy = copies[curr];
            cpy->next = copies[curr->next];
            cpy->random = copies[curr->random];
            curr = curr->next;
        }

        return copies[head];
    }
};
