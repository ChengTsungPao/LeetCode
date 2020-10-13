int numTeams(int* rating, int ratingSize){
    int ans = 0;
    for(int i = 0;i < ratingSize;i++){
        for(int j = i+1;j < ratingSize;j++){
            for(int k = j+1;k < ratingSize;k++){
                if((rating[i] < rating[j] && rating[j] < rating[k]) || (rating[i] > rating[j] && rating[j] > rating[k])){
                    ans++;
                }
            }
        }        
    }
    return ans;
}