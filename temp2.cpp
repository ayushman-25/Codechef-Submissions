#include <bits/stdc++.h>
using namespace std;
#define ll  long long
#define int ll
#define vi vector<int>
#define pii pair<int,int>
#define piii pair<pii, int>
#define pb push_back
#define fs first
#define sc second
//#define ONLINE_JUDGE
#define endl "\n"
#define pow2(i) (1<<(i))  
#define d0(x) cout<<x<<" "
#define d1(x) cout<<(x)<<endl
#define d2(x,y) cout<<(x)<<" "<<(y)<<endl
#define d3(x,y,z) cout<<x<<" "<<y<<" "<<z<<endl
#define d4(x,y,z,w) cout<<x<<" "<<y<<" "<<z<<" "<<w<<endl
#define d5(x,y,z,w,s) cout<<x<<" "<<y<<" "<<z<<" "<<w<<" "<<s<<endl
#define fifo ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define precise(x) cout<<fixed<<setprecision(x)
#define all(v) (v).begin(),(v).end()
const int mod = 1e9+7;
 
 

void solve()
{
    int n,k;
    cin>>n>>k; k--;

    int x = 0; int ans=0;
    for(int i=1;i<=n;i++)
    {
        int y;cin>>y;
        y=y^x; 
        x=x^y;
        //cout<<y<<" "<<x<<endl;
        if(y&pow2(k))
            ans++;
    }
    cout<<ans<<endl;
}
 
 
 
signed main()
{
    // #ifndef ONLINE_JUDGE
    // freopen("input.txt", "r", stdin);
    // //freopen("output.txt", "w", stdout);
    // #endif
 
    fifo
    int t=1;
    cin>>t;

 
    for(ll tc=1;tc<=t;++tc)
    {
        solve();
    }
}
