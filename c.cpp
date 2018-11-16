#include<bits/stdc++.h>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int cost;
  int t,n,m;
  cin>>t;
  while(t--){
    cost=0;
    cin >> n >> m;

    char a[n][m];
    for(int i=0;i<n;i++){
      for(int j=0;j<m;j++){
        cin>>a[i][j];
      }
    }

    if(n==2){
        i=1;
        for(int j=1;j<m-1;j++){
            if(a[i][j]=='G'){
                    if(a[0][j-1]=='R'){cost+=5;}
                    if(a[0][j+1]=='R'){cost+=5;}
                    if(a[0][j+1]=='R'){cost+=5;}
                    if(a[1][j+1]=='G'){cost+=3;}
                    if(a[1][j-1]=='G'){cost+=3;}
                }
                if(a[0][j]=='R'){
                    if(a[0][j-1]=='G'){cost+=3;}
                    if(a[0][j+1]=='G'){cost+=3;}
                    if(a[0][j+1]=='G'){cost+=3;}
                    if(a[0][j-1]=='G'){cost+=3;}
                    if(a[0][j]=='R' ){cost+=5;}
                    if(a[0][j]=='R'){cost+=5;}
                    if(a[0][j+1]=='R'){cost+=5;}
                    if(a[0][j-1]=='R'){cost+=5;}
                }
        }
    }
    else{
        for(int i=1;i<n-1;i++){
            for(int j=1;j<m-1;j++){
                if(a[i][j]=='G'){
                    if(a[i-1][j-1]=='R'){cost+=5;}
                    if(a[i-1][j+1]=='R'){cost+=5;}
                    if(a[i+1][j+1]=='R'){cost+=5;}
                    if(a[i+1][j-1]=='R'){cost+=5;}
                    if(a[i+1][j]=='G'){cost+=3;}
                    if(a[i-1][j]=='G'){cost+=3;}
                    if(a[i][j+1]=='G'){cost+=3;}
                    if(a[i][j-1]=='G'){cost+=3;}
                }
                if(a[i][j]=='R'){
                    if(a[i-1][j-1]=='G'){cost+=3;}
                    if(a[i-1][j+1]=='G'){cost+=3;}
                    if(a[i+1][j+1]=='G'){cost+=3;}
                    if(a[i+1][j-1]=='G'){cost+=3;}
                    if(a[i+1][j]=='R' ){cost+=5;}
                    if(a[i-1][j]=='R'){cost+=5;}
                    if(a[i][j+1]=='R'){cost+=5;}
                    if(a[i][j-1]=='R'){cost+=5;}
                }
            }
        }
    }
    cout<< cost << "\n";
  }
  return 0;
}
