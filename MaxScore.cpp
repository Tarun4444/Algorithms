#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--){
	  int n;
	  cin >> n;
	  long long int a[n],b[n][n];
	  for(int i=0;i<n;i++){
	      for(int j=0;j<n;j++){
	            cin>>a[j];
	      }
	      sort(a,a+n);
	      for(int j=0;j<n;j++){
	          b[i][j]=a[j];
	      }
	   }
	  long long int max=b[n-1][n-1];
	  for(int i=n-2;i>=0;i++){
	    for(int j=0;j<n;j++){
	       if(b[i][j] > max){
	           x=
	           break;
	       else flag=1;
	    }
	    sum+=x;
	  }
	}
	return 0;
}
