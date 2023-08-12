class Solution{
public:
    string finalString(string s) {
        int n = s.size();
        
        bool isLeft = false;
        string left, right;
        for(int i = n - 1; i >= 0; i--){
            if(s[i] == 'i'){
                isLeft = !isLeft;
            } else if (isLeft) {
                left.push_back(s[i]);
            } else {
                right.push_back(s[i]);
            }
        }
        reverse(right.begin(), right.end());

        return left + right;
    }
};