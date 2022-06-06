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

template<typename T, typename U> inline void amin(T &x, U y) {if (y < x) x = y;}
template<typename T, typename U> inline void amax(T &x, U y) {if (x < y) x = y;}

// REF - https://codeforces.com/blog/entry/62393
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

void solve() {
    int n, m;
    cin >> n >> m;
    cout << "here\n";
    vector<set<int>> frnd;
    frnd.resize(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        frnd[a].insert(b);
        frnd[b].insert(a);
    }
    int ans = 0;
    unordered_map<int, int, custom_hash> to_be_dead;
    for (int i = 1; i < n + 1; i++) {
        if (*frnd[i].rbegin() > i) {
            ans++;
            to_be_dead[i] = 1;
        }
    }
    int q; cin >> q;
    while (q--) {
        int oper; cin >> oper;
        if (oper == 1 || oper == 2) {
            int u, v;
            cin >> u >> v;
            if (oper == 1) {
                frnd[u].insert(v);
                frnd[v].insert(u);
                if (!to_be_dead[u] && v > u) {
                    ans++;
                    to_be_dead[u] ^= 1;
                }
                if (!to_be_dead[v] && u > v) {
                    ans++;
                    to_be_dead[v] ^= 1;
                }
            } else {
                frnd[u].erase(v);
                frnd[v].erase(u);
                if (to_be_dead[u] && u > *frnd[u].rbegin()) {
                    to_be_dead[u] ^= 1;
                    ans--;
                }
                if (to_be_dead[v] && v > *frnd[v].rbegin()) {
                    to_be_dead[v] ^= 1;
                    ans--;
                }
            }
        } else {
            cout << n - ans << "\n";
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
    while (t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    // cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    return 0;
}