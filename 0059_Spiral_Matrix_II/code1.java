class Solution {
    public int[][] generateMatrix(int n) {
        int[][] data = new int[n][n];
        int count=1;
        int row=0,col=0;
        for(row=0;row<n/2;row++){
            for(col=row;col<n-row-1;col++){
                data[row][col]=count++;
            }
            for(col=row;col<n-row-1;col++){
                data[col][n-row-1]=count++;
            }                
            for(col=n-row-1;col>row;col--){
                data[n-row-1][col]=count++;
            }
            for(col=n-row-1;col>row;col--){
                data[col][row]=count++;
            } 
        }
        if(n%2!=0){
            data[n/2][n/2]=count++;
        }
        return data;
    }
}