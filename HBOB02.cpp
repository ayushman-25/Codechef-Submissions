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
    ll n, k;
    cin >> n >> k;
    vector<ll> b(n);
    for(ll &inp: b) cin >> inp;
    vector<ll> my = {b[0]};
    ll curr_xor = 0;
    for(int i = 0; i < n; i++) {
        curr_xor ^= my.back();
        my.push_back(curr_xor ^ b[i]);
    }
    ll cnt = 0;
    for(ll i: my) {
        cnt += ((i >> (k - 1)) & 1);
    }
    cout << cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int t = 1, casee = 1;
    // cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    return 0;
}