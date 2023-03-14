#include<bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cout.tie(0);
    vector<pair<int, char>> ans(26, {0, 'A'});
    int ti;
    cin >> ti;
    for (int i = 0; i < 26;++i)
    {
        ans[i].second += i;
    }
    cin.get();
        string in_;
        for (int k = 0; k < ti; k++)
        {
            getline(cin , in_);
            transform(in_.begin(), in_.end(), in_.begin(), ::tolower);
            for (auto& i:in_)
            {
                if(isalpha(i)){
                    ans[i-'a'].first++;
                }
            }
        }
        sort(ans.begin(), ans.end(), [](auto& a, auto& b)->bool {
        if(a.first==b.first)
        {
            return a.second < b.second;
        }
        return a.first > b.first;
    });
    for(auto i:ans)
    {
        if(i.first==0)
        {
            break;
        }
        cout << i.second << " " << i.first << endl;
        
    }

    
    
    system("pause");
}