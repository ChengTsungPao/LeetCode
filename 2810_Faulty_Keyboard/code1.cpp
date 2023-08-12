class Solution{
public:
    string finalString(string s) {
        int n = s.size();

        string cur_s = "";
        for(int i = 0; i < n; i++){
            if(s[i] == 'i'){
                reverse(cur_s.begin(), cur_s.end());
            } else {
                cur_s.push_back(s[i]);
            }
        }

        return cur_s;
    }
};