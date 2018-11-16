#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
long long x,m;
long long int M[2][2] = {{1,1},{1,0}};

void multiply(long long F[2][2], long long M[2][2])
{
  long long x =  F[0][0]*M[0][0] + F[0][1]*M[1][0];
  long long y =  F[0][0]*M[0][1] + F[0][1]*M[1][1];
  long long z =  F[1][0]*M[0][0] + F[1][1]*M[1][0];
  long long w =  F[1][0]*M[0][1] + F[1][1]*M[1][1];
  F[0][0] = x%m;
  F[0][1] = y%m;
  F[1][0] = z%m;
  F[1][1] = w%m;
}
void power(long long F[2][2], long long n)
{
  if(n ==0||n==1)
    return;
  power(F, n/2);
  multiply(F, F);
  if (n%2 != 0)
	multiply(F, M);
}
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
  	cin>>x>>m;
  	long long int F[2][2] = {{1,1},{1,0}};
  	if(x==1||x==2)
  	cout<<2%m<<endl;
  	else
  	{
  	power(F,x-1);
  	cout<<(2*F[0][0])%m<<endl;
  	}
  	}
  return 0;
} 
