#include<iostream>
#include<iomanip>
#include<fstream>
#include<string>

using namespace std;

int main(){
    int sum =0 
    string x;
    ifstream infile;

    infile.open("input.txt");
    if(!infile){
        cout << "Unable to open file"
        exit(1)
    }

    while(infile >> x){
        cout << x
    }

    infile.close()
    return 0
}