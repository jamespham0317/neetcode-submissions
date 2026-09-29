class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        int res = 1;
        sort(nums.begin(), nums.end());

        int idx = 1;
        while (idx < nums.size() && nums[idx] == nums[idx - 1]) {
            idx++;
        }

        int length = 1;
        while (idx < nums.size()) {
            if (nums[idx] - 1 == nums[idx - 1]) {
                length++;
            } else {
                length = 1;
            }
            res = max(res, length);
            idx++;
            while (idx < nums.size() && nums[idx] == nums[idx - 1]) {
                idx++;
            }
        }

        return res;
    }
};
