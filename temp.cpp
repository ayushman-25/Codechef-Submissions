#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long ull;
 
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
ll myRand(ll B) {
    return (ull)rng() % B;
}

int main(){
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int q; cin >> q;
    while(q--){
        int n; cin >> n;
        vector<int> a(n);
        for(int i=0;i<n;i++){
            cin >> a[i];
        }
        vector<int> d(n,1e9);
        d[0]=0;
        deque<int> q;
        q.push_back(0);
        while(q.size()){
            int p=q.front(); q.pop_front();
            if(p>0 and d[p-1]>d[p]){
                d[p-1]=d[p];
                q.push_front(p-1);
            }
            int nx=min(n-1,p+a[p]);
            if(d[nx]>d[p]+1){
                d[nx]=d[p]+1;
                q.push_back(nx);
            }
        }
        if(d[n-1]==1e9)d[n-1]=-1;
        cout << d[n-1] << "\n";
    }
}