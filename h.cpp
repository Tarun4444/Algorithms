#include<iostream>
using namespace std;

long long int a[10000]={0};
int agon(int n){
  long long int c=0;
  if(a[n]!=0){
    return a[n];
  }
  for(int i=1;i<=n;i+=2){
    c+=agon(n-i);
  }
  a[n]=c;
  return a[n];
}
int main(){
  std::ios_base::sync_with_stdio(false);
  int n,m,t;
  a[0]=2;
  a[1]=2;
  cin >> t;
  while(t--){
    cin >> n >> m;
    cout<< agon(n)%m <<"\n";
  }
  return 0;
}
