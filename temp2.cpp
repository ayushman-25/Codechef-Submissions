#include <bits/stdc++.h>
typedef long long int ll;
#define fastio ios::sync_with_stdio(false), cin.tie(NULL);
using namespace std;

int main() {
    fastio
int t;
cin>>t;
//while(t--)
//{
//     int n;
//     cin>>n;
    string s;
    while(cin>>s)
    {
    reverse(s.begin(), s.end()); 
    for (int i = 0; i < s.size(); i++)
            s[i] = tolower(s[i]);
    cout<<s;
    cout<<"\n";
    }
    
//}
return 0;

}