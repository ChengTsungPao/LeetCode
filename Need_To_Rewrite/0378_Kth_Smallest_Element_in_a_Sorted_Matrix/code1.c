int kthSmallest(int** matrix, int matrixSize, int* matrixColSize, int k){
    int ans[matrixSize*matrixSize];
    int tmp[matrixSize];
    int temp,flag,index;
    if(matrixSize*matrixSize>2*k){
        for(int i=0;i<matrixSize;i++){
            ans[i] = matrix[0][i];
            tmp[i] = 0;
        }
        for(int i=1;i<matrixSize;i++){
            temp = i*matrixSize;
            index = 0;
            for(int j=0;j<matrixSize;j++){           

                if(tmp[0]>k){
                    return ans[k-1];
                }
                flag = 0;
                for(int n=tmp[j];n<temp;n++){
                    if(matrix[i][j]<=ans[n]){
                        for(int m=temp-1;m>=n;m--){
                            ans[m+1] = ans[m];                       
                        }
                        ans[n] = matrix[i][j];
                        tmp[index++] = n;
                        temp++;
                        flag=1;
                        break;

                    }
                }
                if(flag==0){
                    ans[temp] = matrix[i][j];
                    tmp[index++] = temp;
                    temp++;
                }
            }            
        } 
        return ans[k-1];
    }else{
        for(int i=0;i<matrixSize;i++){
            ans[i] = matrix[0][matrixSize-i-1];
            tmp[i] = 0;
        }
        for(int i=matrixSize-1;i>0;i--){
            temp = ((matrixSize-1)-i+1)*matrixSize;
            index = 0;
            for(int j=matrixSize-1;j>=0;j--){           

                if(tmp[0]>matrixSize*matrixSize-k){
                    return ans[matrixSize*matrixSize-k];
                }
                flag = 0;
                for(int n=tmp[matrixSize-1-j];n<temp;n++){
                    if(matrix[i][j]>=ans[n]){
                        for(int m=temp-1;m>=n;m--){
                            ans[m+1] = ans[m];                       
                        }
                        ans[n] = matrix[i][j];
                        tmp[index++] = n;
                        temp++;
                        flag=1;
                        break;

                    }
                }
                if(flag==0){
                    ans[temp] = matrix[i][j];
                    tmp[index++] = temp;
                    temp++;
                }

            }
        }
        return ans[matrixSize*matrixSize-k];
    }
    return 0;
    
}