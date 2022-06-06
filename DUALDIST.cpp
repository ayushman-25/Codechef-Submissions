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

// REFERENCES - CPALGORITHMS (nlogn precomputation of LCA using segtree)

int n, l, timer;
vector<vector<int>> adj, up;
vector<int> tin, tout;

void dfs(int v, int p) {
    tin[v] = ++timer;
    up[v][0] = p;
    for (int i = 1; i <= l; ++i) {
        up[v][i] = up[up[v][i-1]][i-1];
    }
    for (int u : adj[v]) {
        if (u != p) dfs(u, v);
    }
    tout[v] = ++timer;
}

bool is_ancestor(int u, int v) {
    return tin[u] <= tin[v] && tout[u] >= tout[v];
}

int lca(int u, int v) {
    if (is_ancestor(u, v)) return u;
    if (is_ancestor(v, u)) return v;
    for (int i = l; i >= 0; --i) {
        if (!is_ancestor(up[u][i], v)) u = up[u][i];
    }
    return up[u][0];
}

void preprocess(int root) {
    tin.resize(n);
    tout.resize(n);
    timer = 0;
    l = ceil(log2(n));
    up.assign(n, vector<int>(l + 1));
    dfs(root, root);
}

void solve() {
	int q;
	cin >> n >> q;
	adj.resize(n);
	for(int i = 0; i < n - 1; i++) {
		int u, v;
		cin >> u >> v;
		u--; v--;
		adj[u].emplace_back(v);
		adj[v].emplace_back(u);
	}
    preprocess(0);
	vector<int> myDep(n, 0), vis(n, 0);
	vis[0] = 1;
	queue<int> qu;
	qu.push(0);
	while(!qu.empty()) {
		int par = qu.front();
		qu.pop();
		for(auto i: adj[par]) {
			if(!vis[i]) {
				qu.push(i);
				vis[i] = 1;
				myDep[i] = myDep[par] + 1;
			}
		}
	}
	for(int i = 0; i < q; i++) {
		int a, b;
		cin >> a >> b;
		a--; b--;
		ll ans = 0;
		for(int j = 0; j < n; j++) {
			ans += min((myDep[j] + myDep[a] - (myDep[lca(j, a)] << 1)), (myDep[j] + myDep[b] - (myDep[lca(j, b)] << 1)));
		}
		cout << ans << "\n";
	}
    adj.clear();
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