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
    ll n, m, s, k;
    cin >> n >> m >> s >> k;
    vector<vector<ll>> adj;
    adj.resize(n + 1);
    for(int i = 0; i < m; i++) {
        ll x, y;
        cin >> x >> y;
        adj[x].emplace_back(y);
        adj[y].emplace_back(x);
    }
    vector<ll> visited(n + 1, 0);
    vector<ll> depth(n + 1, 0);
    queue<ll> q;
    q.push(0);
    visited[0] = 1;
    while(!q.empty()) {
        ll par = q.front();
        q.pop();
        for(ll i: adj[par]) {
            if(!visited[i]) {
                q.push(i);
                depth[i] = depth[par] + 1;
                visited[i] = 1;
            }
        }
    }
    vector<ll> builds(s);
    for(ll& i: builds) cin >> i;
    vector<int> check;
    for(ll i: builds) {
        check.emplace_back(depth[i]);
    }
    sort(check.begin(), check.end());
    ll ans = 0;
    for(int i = 0; i < k; i++) {
        ans += check[i];
    }
    cout << (ans << 1) << "\n";
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