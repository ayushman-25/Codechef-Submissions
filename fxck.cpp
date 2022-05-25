/*

*  Author : Ayushman Chahar  #
*  About  : IT Junior        #
*  Insti  : VIT, Vellore     #

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
    map<string, int> dd;
    int n;
    cin >> n;
    while(n--) {
        string s;
        cin >> s;
        int start = 1;
        if(dd[s]) {
            string copy = s;
            while(1) {
                copy += to_string(start);
                if(!dd[copy]) break;
                copy = copy.substr(0, s.size() - 1);
                start++;
            }
            cout << copy << "\n";
            dd[copy] = 1;
        } else {
            cout << "OK\n";
            dd[s] = 1;
        }
    }
}

int main() {
// #ifndef ONLINE_JUDGE
//     freopen("in.txt", "r", stdin);
//     freopen("out.txt", "w", stdout);
//     freopen("error.txt", "w", stderr);
// #endif
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int t = 1, casee = 1;
    // cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    // cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    return 0;
}