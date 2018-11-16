#include <bits/stdc++.h>
#include<string>
using namespace std;

int main() {
    int n;
    cin >> n;
    int alpha,flag;
    int min=INT_MAX;
    string nam;
    alpha=0;
    for(int a0 = 0; a0 < n; a0++){
        string name;
        int value,a=0,b=0;
        cin >> name >> value;
        string val=to_string(value);
        for(int i=0;i<val.length();i++){
            if(val[i]==4){
                a++;    
                flag=0;
            }
            else if(val[i]==7){
                b++;    
                flag=0;
            }
            else{ 
                flag=1;
                break;
            }
        }
        if(a==b && flag==0)
            if(value<min){
                alpha=1;
                min=value;
                nam=name;
            }
     }
     if(alpha==1) 
         cout<<nam;
     else 
         cout<<"-1";
    return 0;
}
