#include <bits/stdc++.h>
using namespace std;

#define int  long long int //int64_t
#define endl '\n'
#define vint vector<int>
#define pb push_back

#define f(i,a,b) for(int i=(a);i<(b);i++)
#define rf(i,a,b) for(int i=(a);i>(b);i--)

void ritikio();
int T=0;




void solve()
{ 
    int n; cin>>n;
    int j=1;
    while(1)
    {
        if(n%2==1) break;
        else n=n>>1, j++;
    }
    cout<<j<<endl;
}



signed main()
{
    // void ritikio()
    {
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        // #ifndef ONLINE_JUDGE
        #ifdef RITIK
            freopen("input999.txt", "r", stdin);
            freopen("output999.txt", "w", stdout);
            // freopen("error.txt","w",stderr);
            //fclose(stdout);
        #endif
    }
    int TT = 1;
    T = 0;
    cin >> TT;

    while(++T < TT + 1)
    {
        solve();
    }
    
}