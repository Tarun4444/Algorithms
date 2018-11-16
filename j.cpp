#include<iostream>
#include<algorithm>
using namespace std;

int main(){
  std::ios_base::sync_with_stdio(false);
  int n,d,c=0;
  long int a[100000];
  bool b[100000];
  for(int i=0;i<n;i++){
    cin>>a[i];
  }
  for(int i=0;i<n;i++){
    b[i]=false;
  }
   sort(a, a+n, greater<int>());
  for(int i=0;i<n;i++){
    if(b[i]==false){
      if(a[i]-a[i+1]<=d){
        c++;
        b[i+1]=true;
        b[i]=true;
      }
    }
  }
  cout<<c;
return 0;
}
