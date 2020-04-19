bool isInterleave(char * s1, char * s2, char * s3){  
    bool dfs(char * s1, char * s2, char * s3){
        if(*s1==NULL && *s2==NULL && *s3==NULL)
            return true;
        if(*s1!=NULL)
            if(*s1==*s3 && dfs(s1 + 1, s2, s3 + 1))
                return true;
        if(*s2!=NULL)
            if(*s2==*s3 && dfs(s1, s2 + 1, s3 + 1))
                return true;
        return NULL;
    }
    if(strlen(s1)+strlen(s2)==strlen(s3) && dfs(s1, s2, s3))
        return true;
    else
        return false;
}