#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main(){
	int N;
	while(cin >> N){
		int arr[N];
		for (int i =0;  i <N; i++){
			scanf("%d",&arr[i]);
		}
		int max = 0;
		for(int i = 0; i < N; i++){
			int val = 0;
			int j = i;
			while(j< N && arr[j] >= arr[i]){
				val += arr[j];
				j++;
			}
			j = i-1;
			while(j >= 0 && arr[j] >= arr[i]){
				val += arr[j];
				j--;
			}
			if (arr[i]*val > max)max = arr[i] * val;
			
		}
		printf("%d\n", max);
	}
	return 0 ;
}
