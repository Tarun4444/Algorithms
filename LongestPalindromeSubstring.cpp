#include<bits/stdc++.h>
using namespace std;

void longestPalindromeSubstring(char *str){
  int n = strlen(str);
  bool table[i][j];
  memset(table,false,sizeof(table));

  int maxlength=1;
  for(int i=0;i<n;i++)table[i][i]=true;

  int start=0;
  for(int i=0;i<n-1;i++){
    if(str[i]==str[i+1]){
      maxlength=2;
      strat=i;
      table[i][i+1]=2;
    }
  }
  int k=0;

  for(int k=3;k<n;k++){
    for(int i=0;i<n;i++){

      int j=i+k-1;

      if(table[i+1][j-1]=true && str[i]==str[j]){
        table[i][j]=true;
        if(k>maxlength){
          maxlength=k;
          start=i;
        }
      }
    }
  }
  for(int i=start;i<start+maxlength-1;i++)cout<<str[i];
  return maxlength;
}
int main(){
  char str[]="forgeeksskeegfor";
  cout<<longestPalindromeSubstring(str);
  return 0;
}
