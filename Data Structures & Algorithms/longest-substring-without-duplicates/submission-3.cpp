class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        int l   = 0;
        set<int> seen;
        for (int r = 0; r < s.length(); r++) {
            while (seen.find(s[r]) != seen.end() && l < s.length()) {
                seen.erase(s[l]);
                l++;
            }
            seen.insert(s[r]);
            res = res > seen.size() ? res : seen.size();
        }
        return res;
    }
};
