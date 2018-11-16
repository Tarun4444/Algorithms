#include <bits/stdc++.h>
using namespace std;

long a[100];
long sequence(int x){
    if(x%2==1 && x>1){
        a[x]=x+1;
        return a[x];
    }
    a[1]=1;
    a[2]=3;
    for(int i=4;i<=x;i++){
        for(int j=2;j<=x;j++){

        }
    }
    return a[x];
}
long longestSequence(vector <long> a,int n){
    long moves=0;
    for(int i=0;i<n;i++){
        moves=moves + sequence(a[i]);
    }
    return moves;
}
int main() {
    int n;
    cin >> n;
    vector<long> a(n);
    for(int a_i = 0; a_i < n; a_i++){
       cin >> a[a_i];
    }
    long result = longestSequence(a,n);
    cout << result << endl;
    return 0;
}
