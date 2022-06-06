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

int mod_pow(long long x, unsigned int y) {
    int res = 1;
    x %= MOD;
    if (x == 0) return 0;
    while (y) {
        if (y & 1)
            res = (res % MOD * x % MOD) % MOD;
        y >>= 1;
        x = (x % MOD * x % MOD) % MOD;
    }
    return res;
}

void solve() {
	int n, m;
	cin >> n >> m;
	cout << mod_pow((mod_pow(2, n) - 1) % MOD, m) << "\n";
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