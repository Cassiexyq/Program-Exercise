#include<iostream>
#include<stdio.h>

using namespace std;

class Solution{
public:
	// 二分法
	int sqrt(int x){
		if (x < 1) return x;
		int low = 1;
		int high = x / 2;
		while(low < high){
			long mid = low + (high - low) / 2;
			if(mid * mid == x) return mid;
			else if (mid * mid < x){
				if ((mid+1) * (mid+1) > x){
					return mid;
				} 
				low = mid +1;
			}
			else high = mid -1;
		}
		return low;
	}

   //牛顿法
	int sqrt2(int x){
		long a = x;
		long exp = 0.00001;
		while(a*a - x > exp){
			a = 0.5 * ( a + x / a);
		}
		return a;
	}
};
int main(){
	Solution s;
	std::cout << s.sqrt(8) << endl;
	std::cout << s.sqrt2(8) << endl;
	// std::array<double, 10> datas {1,2,3,4};
	// datas.fill(2.0);
	// cout << datas.at[9] << endl;
	// cout << datas.at[10] <<endl;
	// return 0;
}