class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;  
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]=='1'){
                    dfs(grid, i,j);
                    count++;
                }
            }            
        }
        return count;
    }
    
    private void dfs(char[][] grid, int x,int y){
        grid[x][y] = '2';
        if(x+1<grid.length){
            if(grid[x+1][y]=='1'){
                dfs(grid, x+1,y);
            }
        }
        if(y+1<grid[0].length){
            if(grid[x][y+1]=='1'){
                dfs(grid, x,y+1);
            }
        }
        if(x-1>=0){
            if(grid[x-1][y]=='1'){
                dfs(grid, x-1,y);
            }
        }
        if(y-1>=0){
            if(grid[x][y-1]=='1'){
                dfs(grid, x,y-1);
            }
        }
    }
}