/*

*  Author : Ayushman Chahar   #
*  About  : IT Sophomore      #
*  Insti  : VIT, Vellore      #

*/

#pragma GCC optimize("Ofast")  
#pragma GCC target("avx,avx2,fma") 
#pragma GCC optimization ("unroll-loops")

#include<bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define mod 998244353

typedef long long int ll;
typedef unsigned long long int ull;

template<typename T, typename U> inline void amin(T &x, U y) {if(y < x) x = y;}
template<typename T, typename U> inline void amax(T &x, U y) {if(x < y) x = y;}

const int maxn = 207;
int t, d, q;
bool dp[maxn];

void solve() {
        memset(dp, 0, sizeof(dp));
        dp[0] = 1;
        cin >> q >> d;
        if(!d) d += 10;
        int mx =d * 10;
        for (int i = 0; 10 * i + d <= mx; ++i){
            for (int j=0; 10 * i + d + j <= mx; ++j){
                dp[10 * i + d + j] |= dp[j];
            }
        }
        while (q--){
            int u;
            cin >> u;
            if (u >= mx || dp[u]) cout<<"YES\n";
            else cout<<"NO\n";
        }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int t = 1, casee = 1;
    cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    return 0;
}