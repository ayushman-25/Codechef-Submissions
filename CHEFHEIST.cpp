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

void solve() {
	int d, D, p, q;
	cin >> D >> d >> p >> q;
	ll ans = D * p;
	ll n = D / d - 1;
	ans += (n * (n + 1) / 2);
	cout << ans << "\n";
	ans *= d;
	cout << ans << "\n";
	ans *= q;
	cout << ans << "\n";
	if(ceil((long double)D / d) != floor((long double)D / d)) {
		ans -= (D % d) * (D / d) * q * d;
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