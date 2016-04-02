//maim -x 250 -y 25 -w 750 -h 735 -d 5 ~/$(date +%T).png

#include<stdio.h>
	int block[8][8]={
{1, 1, 10, 1, 1, 1, 2, -1, },
{-1, 1, 10, 1, -1, 1, 2, -1, },
{2, 2, 10, 1, 2, 2, 2, 1, },
{-1, 1, 10, 10, 1, -1, 1, 10, },
{1, 1, 10, 10, 2, 2, 2, 10, },
{10, 10, 1, 1, 2, -1, 2, 1, },
{10, 10, 2, -1, 3, 2, 0, 0, },
{10, 10, 2, -1, 2, 1, 0, 0, },
};

void neighbour(int i,int j){
	int hmunop=0;int p,q;
	int hmbbs=0;
	int newno;
	int uo[10][2];
	if(i-1>=0 && j-1>=0){
		if(block[i-1][j-1]==-1){
			hmbbs++;
		}
		if(block[i-1][j-1]==0){
			hmunop++;
			uo[hmunop-1][0]=i-1;
			uo[hmunop-1][1]=j-1;
		}
	}
	if(i-1>=0 && j>=0){
		if(block[i-1][j]==-1){
			hmbbs++;
		}
		if(block[i-1][j]==0){
			hmunop++;
			uo[hmunop-1][0]=i-1;
			uo[hmunop-1][1]=j;
		}
	}
	if(i-1>=0 && j+1<=7){
		if(block[i-1][j+1]==-1){
			hmbbs++;
		}
		if(block[i-1][j+1]==0){
			hmunop++;
			uo[hmunop-1][0]=i-1;
			uo[hmunop-1][1]=j+1;
		}
	}
	if(i>=0 && j-1>=0){
		if(block[i][j-1]==-1){
			hmbbs++;
		}
		if(block[i][j-1]==0){
			hmunop++;
			uo[hmunop-1][0]=i;
			uo[hmunop-1][1]=j-1;
		}
	}
	if(i>=0 && j+1<=7){
		if(block[i][j+1]==-1){
			hmbbs++;
		}
		if(block[i][j+1]==0){
			hmunop++;
			uo[hmunop-1][0]=i;
			uo[hmunop-1][1]=j+1;
		}
	}
	if(i+1<=7 && j-1>=0){
		if(block[i+1][j-1]==-1){
			hmbbs++;
		}
		if(block[i+1][j-1]==0){
			hmunop++;
			uo[hmunop-1][0]=i+1;
			uo[hmunop-1][1]=j-1;
		}
	}
	if(i+1<=7 && j>=0){
		if(block[i+1][j]==-1){
			hmbbs++;
		}
		if(block[i+1][j]==0){
			hmunop++;
			uo[hmunop-1][0]=i+1;
			uo[hmunop-1][1]=j;
		}
	}
	if(i+1<=7 && j+1<=7){
		if(block[i+1][j+1]==-1){
			hmbbs++;
		}
		if(block[i+1][j+1]==0){
			hmunop++;
			uo[hmunop-1][0]=i+1;
			uo[hmunop-1][1]=j+1;
		}
	}
		
	printf("unopened are %d\n and bombs are  %d\n",hmunop,hmbbs);
	newno=block[i][j]-hmbbs;
	if(newno==0){
		//set all unopened boxes as click karo lapak ke
	
		for(p=0;p<=hmunop-1;p++){
			block[uo[p][0]][uo[p][1]]=100;
		}
	}
	if(hmunop-newno==0){
		//set all unopened boxes as bombed
		for(p=0;p<=hmunop-1;p++){
			block[uo[p][0]][uo[p][1]]=-1;
		}
	}

//	return block[8][8];	
			
}


int main()
{
	int i,j;

	for(i=0;i<8;i++){
		for(j=0;j<8;j++){
			if(block[i][j]>=1 && block[i][j]<9){
				neighbour(i,j);
			}
				
		}	
	

	}

	for(i=0;i<8;i++){
		printf("{");
		for(j=0;j<8;j++){
		
			printf("%d, ",block[i][j]);
		}
		printf("},");
		printf("\n");
	}
	return 0;
}




