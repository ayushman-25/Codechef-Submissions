#include<bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define int long long int

vector<vector<pair<int,int> > > graph;
vector<int> lvl,first,euler,dis,tree;
vector<bool> vis;
int n,q,r;

void init(){
    euler.clear();
    cin>>n>>q>>r;
    graph.assign(n+1,{});
    lvl.assign(n+1,0);
    dis.assign(n+1,-1);
    first.assign(n+1,-1);
    vis.assign(n+1,false);
}

void build(int l = 0,int r = euler.size()-1,int i = 0){
    if(l == r) { tree[i] = euler[l]; return; }
    build(l,l+(r-l)/2,2*i+1);
    build(l+(r-l)/2+1,r,2*i+2);
    tree[i] = (lvl[tree[2*i+1]] < lvl[tree[2*i+2]] ? tree[2*i+1] : tree[2*i+2]);
}

int lca(int ql,int qr,int l = 0,int r = euler.size()-1,int i = 0){
    if(ql < 0 or qr > euler.size()-1 or qr < ql or ql > r or qr < l) return 0;
    if(ql <= l and r <= qr) return tree[i];
    int a = lca(ql,qr,l,l+(r-l)/2,2*i+1), b = lca(ql,qr,l+(r-l)/2+1,r,2*i+2);
    return (lvl[a] < lvl[b] ? a : b);
}

void dfs(int src,int d=0){
    lvl[src] = d;
    first[src] = euler.size();
    euler.push_back(src);
    vis[src] = true;
    for(auto {child,w}:graph[src]){
        if(!vis[child]){
            dis[child] = dis[src] + w;
            dfs(child,d+1);
            euler.push_back(src);
        }
    }
}

void solve(){
    init();
    for(int i=0;i<n-1;i++){
        int u,v,w; cin>>u>>v>>w;
        graph[u].push_back({v,w});
        graph[v].push_back({u,w});
    }
    dis[0] = INT_MAX;
    lvl[0] = INT_MAX;
    dis[r] = 0;
    dfs(r);
    tree.assign(4*euler.size()+4,0);
    build();
    while(q--){
        int u,v; cin>>u>>v;
        if(first[u] > first[v]) swap(u,v);
        int x = lca(first[u],first[v]);
        int ans = dis[u] + dis[v] - 2*dis[x];
        cout<<ans<<"\n";
    }
}

signed main(){
    #ifndef ONLINE_JUDGE
    // freopen("C:\\input", "r", stdin);
    // freopen("C:\\output", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int t; cin>>t;
    while(t--) solve();
    return 0;
}