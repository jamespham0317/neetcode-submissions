class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size(), cols = matrix[0].size();

        int l = 0, r = rows - 1;
        while (l <= r) {
            int m = (r - l) / 2 + l;
            if (target < matrix[m][0]) {
                r = m - 1;
            } else if (target > matrix[m][cols - 1]) {
                l = m + 1;
            } else {
                int l1 = 0, r1 = cols - 1;
                while (l1 <= r1) {
                    int m1 = (r1 - l1) / 2 + l1;
                    if (target < matrix[m][m1]) {
                        r1 = m1 - 1;
                    } else if (target > matrix[m][m1]) {
                        l1 = m1 + 1;
                    } else {
                        return true;
                    }
                }
                return false;
            }
        }
        return false;
    }
};
