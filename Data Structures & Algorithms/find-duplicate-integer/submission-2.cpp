class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> seen;
        for (auto n : nums) {
            if (seen.find(n) != seen.end()) {
                return n;
            }
            seen[n] = n;
        }
    }
};
