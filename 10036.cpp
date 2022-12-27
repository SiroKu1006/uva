#include<iostream>
#include<vector>
using namespace std;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cout.tie(0);
    int t , n , k ;
    cin >> t;
    while (t--)
    {
        cin >> n >> k;
        int a[n];
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            a[i] = abs(a[i]);
            if (sum < k)
            {
                sum += a[i]%k;
            }
            else
            {
                sum -= a[i]%k;
            }
        }
        if (sum == k || sum == 0)
        {
            cout << "Divisible" << endl ;
        }
        else
        {
            cout << "Not divisible" << endl;
        }
        
        
        
    }
    

    system("pause");
}