#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int>sums;
void check(int sum){
	if(find(sums.begin(),sums.end(),sum)==sums.end())
		sums.push_back(sum);
}

int main(){
	int sum=0;
	vector<vector<int>>fl={{1,2,3,4},{5,6,7,8},{9,10,11,12}};
	vector<vector<int>>fg=fl;
	vector<vector<int>>sec={{0,-1},{0,1},{1,0},{-1,0}};
	for(int i=0;i<fl.size();i++){
		cout<<i<<" ";
		for(int j=0;j<fl[0].size();j++){
			sum=0;
			for(int tp=0;tp<5;tp++){
				int x=i;
				int y=j;
				for(int k=0;k<4;k++){
					if(x<0||y<0||x==3||y==4)break;
					x+=sec[k][0];
					y+=sec[k][1];
					if(fg[x][y]==0){
						tp--;
						continue;
					}
					cout<<sum<<" ";
					sum+=fg[x][y];
					fg[x][y]=0;
				}		
			}
			check(sum);
			fg=fl;
		}
	}
	return 0;
}