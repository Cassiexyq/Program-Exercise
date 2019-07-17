#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

class Solution {
public:
    int StrToInt(string str) {
		int n = str.size(), s = 1;
		long long res = 0;
		if (!n) return 0;
		if (str[0] == '-') s = -1;
		for(int i = (str[0] == '-' || str[0] == '+')? 1: 0; i < n; ++i){
			if(str[i] < '0' || str[i] > '9') return 0;
			res = res * 10 + (str[i]- '0');
			cout << res << endl;
		}       
		return res * s;
    }
};
int main(){
	Solution s;
	string n;
	cin >> n;
	cout << s.StrToInt(n) << endl;
	return 0 ;
}
