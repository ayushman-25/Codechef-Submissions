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
    vector<ll> arr(n);
    // cout << fixed << setprecision(8);
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    if(n == 1) {
        if(arr[0] <= k) {
            cout << 1;
        } else {
            cout << 0;
        }
        return;
    }
    // cout << fixed << setprecision(8);
    // ll total = n + (factorial(n) / (2 * factorial(n - 2)));
    long double ans = 0;
    for(ll i: arr) {
        if(i <= k) ans++;
    }
    for(int i = 0; i < n; i++) {
        ll sum1 = arr[i];
        for(int j = i + 1; j < n; j++) {
            sum1 += arr[j];
            if(sum1 <= k) ans++;
            else break;
        }
    }
    cout << ans / ((n * (n + 1)) / 2);
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