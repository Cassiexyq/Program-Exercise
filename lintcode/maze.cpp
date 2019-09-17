#include<bits/stdc++.h>
using namespace std;
using namespace std;
const int MAX = 1010;
const int BASE = 500;
const int xx[4] = {-1,0,1,0};
const int yy[4] = {0,-1,,0,1};
class Node{
public:
	Node(int _x = 0, int _y = 0, int _step = 0){
		x = _x;
		y = _y;
		step = _step;
	}
	int x,y;
	int step;
};
bool book[MAX][MAX];

int px,py,N;
int pos(int x){
	return x + BASE;
}

int dfs(){
	Node B(0,0);
	queue<Node> que;
	que.push(B);
	book[B.x][B.y] = true;
	while (!que.empty()){
		Node v = que.front();
		que.pop();
		for (int i = 0 ; i < 4; i++){
			int nx = v.x + xx[i];
			int ny = v.y + yy[i];
			if (nx < -500 || nx > 500 || ny < -500 || ny > 500){
				continue;
			}
			if (!book[pos(nx)][pos(ny)]){
				book[pos(nx)][pos(ny)] = true;
				if (nx == px && ny == py){
					return v.step + 1;
					que.push(Node(nx,ny, v.step+1));
				}
			}
		}
	}
	return -1;
}