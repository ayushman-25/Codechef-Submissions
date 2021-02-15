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

const ll p = 998244353;
const ll N = 2e5 + 2;
vector<ll> fNI(N + 1), nNI(N + 1), fact(N + 1);

void IoN() {
    nNI[0] = nNI[1] = 1;
    for(ll i = 2; i < N + 1; i++) {
        nNI[i] = (nNI[p % i] * (p - p / i) % p);
    }
}

void IoF() {
    fNI[0] = fNI[1] = 1;
    for(ll i = 2; i <= N + 1; i++) {
        fNI[i] = (nNI[i] * fNI[i - 1]) % p;
    }
}

void f() {
    fact[0] = 1;
    for(ll i = 1; i < N + 1; i++) {
        fact[i] = (fact[i - 1] * i) % p;
    }
}

ll bino(ll N, ll R) {
    return ((fact[N] * fNI[R]) % p * fNI[N - R]) % p;
}

void solve() {
    IoN();
    IoF();
    f();
    ll n, q;
    cin >> n;
    vector<ll> arr(n);
    for(ll &inp: arr) cin >> inp;
    vector<vector<ll>> mat(n, vector<ll> (32, 0));
    for(ll i = 0; i < n; i++) {
        ll check = arr[i];
        ll start = 31;
        while(check > 0) {
            mat[i][start] = check & 1;
            check >>= 1;
            start--;
        }
    }
    vector<ll> cnt_1(32, 0);
    for(ll i = 31; ~i; i--) {
        ll cnt = 0;
        for(ll j = 0; j < n; j++) {
            if(mat[j][i]) {
                cnt++;
            }
        }
        cnt_1[i] = cnt;
    }
    vector<ll> pre(n + 1, 0);
    for(ll k = 1; k <= n; k++) {
        ll ans = 0;
        for(ll i = 1; i <= k; i += 2) {
            ll check_1_cnt = i;
            ll check_0_cnt = k - i;
            for(ll j = 31; ~j; j--) {
                ll curr_1_cnt = cnt_1[j];
                ll curr_0_cnt = n - cnt_1[j];
                if(curr_1_cnt < check_1_cnt || curr_0_cnt < check_0_cnt) {
                    continue;
                } 
                ll temp = (((bino(curr_0_cnt, check_0_cnt)) * (bino(curr_1_cnt, check_1_cnt))) % mod * (1 << (31 - j) % mod)) % mod;
                ans = (ans % mod + temp % mod) % mod;
            }
        }
        pre[k] = (pre[k - 1] % mod + ans % mod) % mod;
    }
    cin >> q; 
    while(q--) {
        ll m;
        cin >> m;
        cout << pre[m] << "\n";
    }
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