int numDecodings(char * s){
    int count = 0;
    void dfs(char * str){
        if(*str==NULL){
            count++;
            return NULL;           
        }
        if(0 + 48 < *str)
            dfs(str + 1);
        if(strlen(str)>=2)
            if(*str == 1 + 48 || (*str == 2 + 48 && 0 + 48 <= *(str + 1) && *(str + 1) <= 6 + 48))
                dfs(str + 2);
        return NULL;
    }
    dfs(s);
    return count;
}