class Solution {
public:
    string simplifyPath(string path) {
        
        path += "/";
        
        string folder = "";
        vector<string> stack;
        for(char ch: path){
            if(ch == '/'){
                if(folder == ".."){
                    if(!stack.empty()) stack.pop_back();
                } else if (folder != "."){
                    if(!folder.empty()) stack.push_back(folder);
                }
                folder = "";
            } else {
                folder += ch;
            }
        }
        
        string ans = "";
        for(string s: stack){
            ans += "/" + s;
        }
        
        return (!ans.empty()) ? ans : "/";
    }
};