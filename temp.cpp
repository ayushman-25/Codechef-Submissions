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
    int n,m; cin>>n>>m;
    vint v(n+1,-1); v[0]=0;
    rf(i,n,0)
    {
        // cout<<i<<endl;
        v[i]=i+(n%i);
        int r=v[i];
        int j=i-1;
        while(j>0 && v[j]==-1) v[j]=r+i, j--;
    }
    // f(i,1,n+1) cout<<v[i]<<" "; 
    // cout<<endl;
    if(m>=n) cout<<n<<endl;
    else cout<<v[m]<<endl;
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