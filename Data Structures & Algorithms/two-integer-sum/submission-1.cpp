class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        std::vector<int> res;
        for (int i{}; i < nums.size(); i++) {
            int curr = nums[i];
            int s = target - curr;
            if (seen.find(s) != seen.end()) {
                if (i > seen.find(s)->second) {
                    res.emplace_back(seen.find(s)->second);
                    res.emplace_back(i);
                } else {
                    res.emplace_back(i);
                    res.emplace_back(seen.find(s)->second);
                }
                return res;
            } else {
                seen[nums[i]] = i;
            }
        }
    }
};
