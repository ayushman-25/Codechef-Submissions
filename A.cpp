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


const int N = 1e6 + 1;
vector<int> intime(N, 1), outime(N, 1), vis(N, 0);
vector<vector<int>> adj;
int timer = 0;


void dfs(int vertex) {
    vis[vertex] = 1;
    intime[vertex] = ++timer;
    for(int i: adj[vertex]) {
        if(!vis[i]) dfs(i);
    }
    outime[vertex] = ++timer;
}

void solve() {
    int n, q;
    cin >> n >> q;
    adj.resize(n);
    for(int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        x--; y--;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    dfs(0);
    while(q--) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        cout << (intime[a] < intime[b] && outime[a] > outime[b] ? "YES\n" : "NO\n");
    }
}

int main() {
// #ifndef ONLINE_JUDGE
//  freopen("in.txt", "r", stdin);
//  freopen("out.txt", "w", stdout);
// #endif
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