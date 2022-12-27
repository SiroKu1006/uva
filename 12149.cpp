#include <cmath>
#include <iostream>
using namespace std;

int de(int n){
    if (n==1){
        return 1;
    }
    else { 
        return pow(n,2)+de(n-1);
    }
}

int main(void){
    int i ;
    while(cin >> i){
        if(i==0){
            break;
        }
    cout << de(i) << endl;
    }
}