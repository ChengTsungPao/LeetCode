class Solution {
    public int numIslands(char[][] grid) {
        int ans = 0;  
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                ans += dfs(grid, i, j);
            }            
        }
        return ans;
    }
    
    private byte dfs(char[][] grid, int i, int j){
        if(!(0 <= i && i < grid.length && 0 <= j && j < grid[0].length) || grid[i][j] == '0'){
            return 0;
        }

        grid[i][j] = '0';

        dfs(grid, i + 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i - 1, j);
        dfs(grid, i, j - 1);
        
        return 1;
    }
}