int numIslands(char** grid, int gridSize, int* gridColSize){
    if(gridSize==0) return 0;
  	int i,j,k,m,n,group[gridSize][*gridColSize];
    int flag = 1;
  	k=1;
  	for(j=0;j<*gridColSize;j++)
  	{        
  		if(gridSize!=1) m=1;
  		for(i=0;i<gridSize;i++)
  		{
  			if(grid[i][j]=='1')
  			{
  				group[i][j]=k;
  				m=0;
                flag = 0;
			}
			else
			{
				group[i][j]=0;
				if(gridSize!=1 && flag==0) k=k-m+1;
				m=1;
			}
		}
        if(m==0) k++;
	}
    if(flag){
        k = 0;
    }
    k++;

	int scan;
	for(scan=1;scan<=*gridColSize-1;scan++)
	{ 
		for(i=0;i<gridSize;i++)
		{
			if(group[i][scan]!=0 && group[i][scan-1]!=0)
			{
				for(n=0;n<gridSize;n++)
				{
					if(group[i][scan]==group[n][scan] && i!=n)
					{
						group[n][scan]=group[i][scan-1];		
					}
				}
				group[i][scan]=group[i][scan-1];
			}
		}
	}
	for(scan=*gridColSize-1;scan>0;scan--)
	{ 
		for(i=0;i<gridSize;i++)
		{
			if(group[i][scan]!=0 && group[i][scan-1]!=0)
			{
				for(n=0;n<gridSize;n++)
				{
					if(group[i][scan-1]==group[n][scan-1] && i!=n)
					{
						group[n][scan-1]=group[i][scan];		
					}
				}
				group[i][scan-1]=group[i][scan];	
			}
		}
	} 
	for(scan=1;scan<=*gridColSize-1;scan++)
	{ 
		for(i=0;i<gridSize;i++)
		{
			if(group[i][scan]!=0 && group[i][scan-1]!=0)
			{
				for(n=0;n<gridSize;n++)
				{
					if(group[i][scan]==group[n][scan] && i!=n)
					{
						group[n][scan]=group[i][scan-1];		
					}
				}
				group[i][scan]=group[i][scan-1];
			}
		}
	}
	for(scan=*gridColSize-1;scan>0;scan--)
	{ 
		for(i=0;i<gridSize;i++)
		{
			if(group[i][scan]!=0 && group[i][scan-1]!=0)
			{
				for(n=0;n<gridSize;n++)
				{
					if(group[i][scan-1]==group[n][scan-1] && i!=n)
					{
						group[n][scan-1]=group[i][scan];		
					}
				}
				group[i][scan-1]=group[i][scan];	
			}
		}
	} 
    int ans[k];
    for(i=0;i<k;i++)
	{
        ans[i] = 0;
    }
  	for(j=0;j<*gridColSize;j++)
  	{
  		for(i=0;i<gridSize;i++)
  		{
            ans[group[i][j]]=1;
            

		}
	}  
    ans[0] = 0;
    for(i=1;i<k;i++)
	{
        ans[0] += ans[i];
    }
    return ans[0];
}