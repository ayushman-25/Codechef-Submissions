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
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int &i: arr) cin >> i;
    double ans = 0;
    for(int i: arr) {
        if(i == 100) ans += 10;
        else if(i == 99) ans += 9;
        else if(i == 98) ans += 8;
        else if(i == 97) ans += 7;
        else if(i == 96) ans += 6;
        else if(57 <= i && i <= 95) ans += 5;
        else ans += 4;
    }
    cout << ans / n << "\n";
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