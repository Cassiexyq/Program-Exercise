#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
struct P{
	int x,y;
};
bool cmp(P x, P y){
	return x.x > y.x;
}
int main(){
	int n;
	cin >> n;
	P p[n],res[n];
	int x,y;
	for (int i = 0; i < n; i++){
		scanf("%d%d", &x, &y);
		p[i].x = x;
		p[i].y = y; 
	}
	sort(p,p+n,cmp);
	int len = 1;
	int maxy = p[0].y;
	res[0].x = p[0].x;
	res[0].y = p[0].y;
	for(int i = 1; i< n; i++){
		if (p[i].y > maxy){
			maxy = p[i].y;
			res[len].x = p[i].x;
			res[len].y = p[i].y;
			len++;
		}
		
	} 
	for (int i = len-1; i >=0; i--){
		printf("%d %d\n", res[i].x,res[i].y);
	}
	return 0;
}
