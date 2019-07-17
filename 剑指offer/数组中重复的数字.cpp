#include<iostream>EaEasy
#include<stdio.h>
#include<vector>
#include<deque>
using namespace std;

int main(){
	vector<double> v;
	v.reserve(10);
	v[0] = 3.14;
	v[1] = 2.8;
	cout << v.size() << endl;
	v.push_back(3.3);
	cout << v.size() << endl;
	cout << v.back()<<endl;
	std::deque<int> nums;
	nums.push_back(2);

	return 0;
}