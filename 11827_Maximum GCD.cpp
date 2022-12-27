#include<iostream>
#include<sstream>
#include<vector>
using namespace std;

int f( int a, int b )
{
    if( b==0 )
        return a;
    return f( b, a%b );
}

int main()
{
    int a, b,times;
    cin >> times;
    for (int i = 0; i < times; i++)
    {
    cin >> a >> b;
    cout << f(a,b) << endl;
    return 0;
    }
    


}