#include<iostream>
#include <algorithm>
using namespace std;

int main() {
    int t,n,element;
    int a[1000005];
    cin >> t ;
    while(t--){
        cin >> n;
        for(int i=0;i<n;i++){
            cin >> a[i];
        }
        if(next_permutation(a,a+n)){
	        for(int i=0;i<n;i++){
	            cout<< a[i] ;
	        }
	        cout <<"\n";
        }
	    else{
	    	cout<<"-1"<<"\n";
	    }
    }
	return 0;
}
