class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        
        string merge;
        int i = 0, j = 0;
        while(i < m || j < n){
            if((i < m && (i + j) % 2 == 0) || j >= n){
                merge.push_back(word1[i]);
                i += 1;
            } else {
                merge.push_back(word2[j]);
                j += 1;
            }
        }
        
        return merge;        
    }
};