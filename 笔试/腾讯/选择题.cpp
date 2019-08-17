#include<stdio.h>
  
class A
{
	public:
		A(){ 
			printf("A");
		}
		~A(){ printf("~A");}
};
class B:public A
{
	public:
	B(){ printf("B");}
	~B(){ printf("~B");}
};
  
int main()
{
	A*c = new B[2];
	delete[] c;
	return 0;
}