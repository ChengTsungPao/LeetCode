class Solution {
public:
    string decodeAtIndex(string s, int k) {
        int n = s.size();
        s += "1";
        
        string cur_s = "";
        vector<string> vec_s;
        vector<int> vec_length;
        
        long long length = 0;
        for(int i = 0; i < n; i++){
            char ch = s[i];
            if('9' >= ch && ch >= '1'){
                vec_s.push_back(cur_s);
                vec_length.push_back(length);
                
                length = length * (ch - '0');
                if(length >= k) break;
                cur_s = "";
            } else {
                length++;
                cur_s.push_back(ch);
            }
        }

        int m = vec_s.size();
        if(m == 0){
            return {s[k - 1]};
        }
        
        for(int i = m - 1; i >= 0; i--){
            string cur_s = vec_s[i];
            int length = vec_length[i];
            k = k % length;
            
            if(i == 0){
                return {(k > 0) ? cur_s[k - 1] : cur_s.back()};
            }
            
            if(k == 0 && cur_s.size() > 0){
                return {cur_s.back()};
            }
            int idx = k - (length - cur_s.size());
            if(0 < idx && idx < cur_s.size()){
                return {cur_s[idx - 1]};
            }
        }
        
        return "";
    }
};