#include<iostream>
using namespace std;

int gcd(int a,int b){
    if(a==0 || b==0)
        return 0;
    if(a==b)
        return a;
    if(a>b)
      return gcd(a-b,b);
    return gcd(a,b-a);
}
int main(){
    int a=0,b=0;
    cin >> a >> b;
  //  cout<< a << b;
    cout<< gcd(a,b);
}
