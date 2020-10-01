int totalFruit(int* tree, int treeSize){
    int kind[2] = {-1,-1};
    int max = 0;
    int index = 0;
    int same[2] = {tree[0],0};
    int flag = 0;
    for(int i=0;i<treeSize;i++){
        flag = 1;
        if(kind[0]==-1){
            kind[0] = tree[i];
            index++;
            flag = 0;
        }else if(kind[1]==-1 && kind[0]!=tree[i]){
            kind[1] = tree[i];
            index++;
            flag = 0;
        }else if(kind[0]!=-1 && kind[1]!=-1 && tree[i]!=kind[0] && tree[i]!=kind[1]){
            if(max < index){
                max = index;
            }
            index = same[1];
            kind[0] = same[0];
            kind[1] = tree[i];
            same[0] = tree[i];
            same[1] = 0;
        }
        if(tree[i]==same[0]){
            same[1]++;
            if(flag){
                index++;                
            }            
        }else{
            same[0] = tree[i];
            same[1] = 1;
            if(flag){
                index++;                
            }   
        }
    }
    if(max < index){
        max = index;
    }
    return max;
}
