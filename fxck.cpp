#include <bits/stdc++.h>
using namespace std;
int match[501], vis[501];

vector< int > e[501];

int se( int x ) {
    if ( vis[x] ) return 0;
    vis[x] = 1;
    for ( int i = 0; i < (int)e[x].size(); ++i ) {
        int w = e[x][i];
        if ( match[w] == -1 || se( match[w] ) ) {
            match[w] = x;
            return 1;
        }
    }
    return 0;
}

void solve(int n, int m) {
    int tl[n + 1], tr[n + 1];
    int ll[n + 1], hh[n + 1];
    for ( int i = 0; i < n; ++i ) {
        ll[i] = tl[i] = 0;
        hh[i] = tr[i] = n - 1;
    }
    for ( int i = 0; i < m; ++i ) {
        int t, x, y, v;
        cin >> t >> x >> y >> v;
        --x, --y, --v;
        tl[v] = max( tl[v], x );
        tr[v] = min( tr[v], y );
        for ( int j = x; j <= y; ++j ) {
            if ( t == 1 ) hh[j] = min( hh[j], v );
            else ll[j] = max( ll[j], v );
        }
    }
    memset( match, -1, sizeof match );
    for ( int i = 0; i < n; ++i )
        for ( int j = tl[i]; j <= tr[i]; ++j )
            if ( i >= ll[j] && i <= hh[j] )
                e[i].push_back(j);
    int flag = 1;
    for ( int i = 0; i < n && flag; ++i ) {
        memset( vis, 0, sizeof vis );
        flag = se(i);
    }
    if (!flag) {
        cout << -1 << "\n";
        return;
    }
    for ( int i = 0; i < n; ++i )
        cout << match[i] + 1 << " \n"[i + 1 == n];
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    solve(n, m);
    return 0;
}
