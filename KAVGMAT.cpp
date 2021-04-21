/*

*  Author : Ayushman Chahar   #
*  About  : IT Sophomore      #
*  Insti  : VIT, Vellore      #

*/

#pragma GCC optimize("Ofast")  
#pragma GCC target("avx,avx2,fma") 
#pragma GCC optimization ("unroll-loops")
#pragma GCC optimize "trapv"

#include<bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define mod 998244353

typedef long long int ll;
typedef unsigned long long int ull;

template<typename T, typename U> inline void amin(T &x, U y) {if(y < x) x = y;}
template<typename T, typename U> inline void amax(T &x, U y) {if(x < y) x = y;}

void solve() {
    int n, m, avg;
    cin >> n >> m >> avg;
    vector<vector<ll>> mat;
    for(int i = 0; i < n; i++) {
        vector<ll> t(m);
        for(ll &inp: t) cin >> inp;
        mat.emplace_back(t);
    }
    vector<vector<ll>> mat_prefix(n, vector<ll> (m, 0));
    for(int i = 0; i < m; i++) {
        mat_prefix[0][i] = mat[0][i];
    }
    for(int i = 1; i < n; i++) {
        for(int j = 0; j < m; j++) {
            mat_prefix[i][j] = mat[i][j] + mat_prefix[i - 1][j];
        }
    }
    for(int i = 0; i < n; i++) {
        for(int j = 1; j < m; j++) {
            mat_prefix[i][j] += mat_prefix[i][j - 1];
        }
    }
    ll ans = 0;
    for(int length = 0; length < n; length++) {
        for(int row = 0; row < min(n, n - length); row++) {
            if(!length) {
                int posi = lower_bound(mat[row].begin(), mat[row].end(), avg) - mat[row].begin();
                ans += m - min(m, posi);
                continue;
            }
            for(int column = 0; column < min(m, m - length); column++) {
                int a1, a2, a3, a4;
                a1 = row; a2 = column;
                a3 = a1 + length; a4 = a2 + length;
                long double r = mat_prefix[a3][a4];
                if (a1 > 0) r -= mat_prefix[a1 - 1][a4];
                if (a2 > 0) r -= mat_prefix[a3][a2 - 1];
                if (a1 > 0 && a2 > 0) r += mat_prefix[a1 - 1][a2 - 1];
                if ((r / ((length + 1) * (length + 1))) >= avg) {
                    ans += m - a4;
                    break;
                }
            }
        }
    }
    cout << ans << "\n";
}

int main() {
// #ifndef ONLINE_JUDGE
//  freopen("in.txt", "r", stdin);
//  freopen("out.txt", "w", stdout);
// #endif
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