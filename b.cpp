#include <iostream>
#include<string>
#include <cmath>
using namespace std;

#define MAX 500

int res[MAX];
int res_size;

int factorial(int n);
int multiply(int x, int res[], int res_size);

int main(){
    int t;
    cin>>t;
    while(t--){
        int A=0,B=0,D=0,C=0,N=0,M=0,R=0,I=0,J=0;
        J=(pow(10,7)+19);
        cin >> N >> M >> R;
        for(int i=1 ;i<=R-1;i++){
            A=(factorial(N)/(factorial(N-i)*factorial(i)))%J;
            B=(factorial(M)/(factorial(M-R-i)*factorial(R-i)))%J;
            D=(R-i)%J;
            I=i%J;
            C+=((A*B*I*D)%J);
        }
        cout<< (C % J)<<"\n";
    }
    return 0;
}

void factorial(int n)
{
    res[0] = 1;
    res_size = 1;

    for (int x=2; x<=n; x++)
        res_size = multiply(x, res, res_size);
    /*
    for (int i=res_size-1; i>=0; i--)
        cout << res[i];*/
}

int multiply(int x, int res[], int res_size)
{
    int carry = 0;
    for (int i=0; i<res_size; i++)
    {
        int prod = res[i] * x + carry;
        res[i] = prod % 10;
        carry  = prod/10;
    }

    // Put carry in res and increase result size
    while (carry)
    {
        res[res_size] = carry%10;
        carry = carry/10;
        res_size++;
    }
    return res_size;
}
