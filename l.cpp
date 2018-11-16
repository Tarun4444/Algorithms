#include<iostream>
using namespace std;

int main(){
  std::ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t;
  cin>>t;
  while(t--){
    int n,d,a[100000];
    cin >> n >> d;
    for(int i=0;i<n;i++){
      cin>>a[i];
    }
    int b=0,max=a[0];
    for(int i=0;i<n;i++){
      if(a[i]>0){
        b++;
      }
      if(a[i]>max){
        max=a[i];
      }
    }
    if(b==0){
        cout<<max;
        continue;
    }

    int x=0,y=0;
    for(int i=0;i<n;i++){
      x=x+a[i];
      if(x<0){
        x=0;
        continue;
      }
      if(y<x)y=x;
    }
    //cout<<y<<" ";
    if(y<d){
        cout<<"-1"<<endl;
        continue;
    }
    x=0;
    y=0;
    int e=0;
    long long int min=1000000000;
    for(int i=0;i<n;i++){
      if(x+a[i]>x){
        e++;
        x=x+a[i];
      }
      if(x+a[i]>a[i]){
        e=1;
        x=a[i];
      }
      if(x>d){
        if(e<min){
            min=e;
        }
      }
    }
    cout<<min<<endl;
  }
  return 0;
}
