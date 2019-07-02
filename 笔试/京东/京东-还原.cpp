#include<iostream>
using namespace std;
typedef long long LL;
const int N = 1e4+10, M = 210;
const LL mod = 998244353;
int a[N];
LL f[N][M][3], s1[M],s2[M];

int main(){
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++){
		cin >> a[i];
	}
	a[0] =1;
	a[n+1] = 1;
	for (int i= 1;i <= 200; i++){
		s1[i] = s2[i] = 1;
	}
	for(int i = 1; i < n +2; i++){
		int s =1,t = 200;
		if(a[i]!=0) s = t = a[i];
		for(int j = s; j <= t; j++){
			f[i][j][0] = (s1[200]- s2[j]) % mod;
			f[i][j][1] = (f[i-1][j][0] + f[i-1][j][1] + f[i-1][j][2]) % mod;
			f[i][j][2] = s1[j-1] % mod;
		}
		for (int j = 1; j <= 200; j++){
			s1[j] = s1[j-1] + f[i][j][0] + f[i][j][1] + f[i][j][2];
			s2[j] = s2[j-1] + f[i][j][0] + f[i][j][1];
		}
	}
	LL res = 0;
	res = (f[n+1][1][0] + f[n+1][1][1]) % mod;
	cout << res << endl;
	return 0;
	
	  
} 
