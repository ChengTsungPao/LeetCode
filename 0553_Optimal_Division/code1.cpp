class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        return recur(nums, 0, nums.size() - 1, true).second;
    }
    
    pair<double, string> recur(vector<int>& nums, int i, int j, bool findMax){
        if(i == j){
            return make_pair(nums[i], to_string(nums[i]));
        }
        
        string combineStr;
        pair<double, string> left, right, combine;
        pair<double, string> ret = findMax ? make_pair(0.0, "") : make_pair(DBL_MAX, "");
        for(int k = i; k < j; k++){
            left = recur(nums, i, k, findMax);
            right = recur(nums, k + 1, j, !findMax);
            combineStr = (k < j - 1) ? left.second + "/" +  "(" + right.second + ")" : left.second + "/" + right.second;
            combine = make_pair(left.first / right.first, combineStr);
            ret = findMax ? maxValuePair(ret, combine) : minValuePair(ret, combine); 
        }
        
        return ret;        
    }
    
    pair<double, string> maxValuePair(pair<double, string> a, pair<double, string> b){
        return (a.first > b.first) ? a : b;
    }
    
    pair<double, string> minValuePair(pair<double, string> a, pair<double, string> b){
        return (a.first < b.first) ? a : b;
    }
};