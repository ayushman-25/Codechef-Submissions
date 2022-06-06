/*

* Author - Ayushman Chahar
* About  - IT Junior, VIT Vellore

*/

#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")

#include "bits/stdc++.h"
using namespace std;

template<typename T, typename U> inline void amin(T &x, U y) {if (y < x) x = y;}
template<typename T, typename U> inline void amax(T &x, U y) {if (x < y) x = y;}

// Ref - Merge Sort Tree,
// https://cp-algorithms.com/data_structures/segment_tree.html
// https://discuss.codechef.com/t/merge-sort-tree-tutorial/14277

const int MAXN = 2e5 + 3;
vector<int> t[MAXN << 2];
vector<int> arr;

void build(int cur, int l, int r) {
  if (l == r) {
    t[cur] = vector<int> (1, arr[l]);
    return;
  }
  int m = (l + r) >> 1;
  build((cur << 1), l, m);
  build((cur << 1) + 1, m + 1, r);
  merge(t[(cur << 1)].begin(), t[(cur << 1)].end(), t[(cur << 1) + 1].begin(), t[(cur << 1) + 1].end(), back_inserter(t[cur]));
}

int query_smaller(int cur, int l, int r, int x, int y, int k) {
  if (r < x || l > y) {
    return 0;
  }
  if (x <= l && y >= r) {
    return lower_bound(t[cur].begin(), t[cur].end(), k) - t[cur].begin();
  }
  int mid = (l + r) >> 1;
  return query_smaller((cur << 1), l, mid, x, y, k) + query_smaller((cur << 1) + 1, mid + 1, r, x, y, k);
}

void solve() {
  int n; cin >> n;
  for (int i = 0; i < n; i++) {
    int x; cin >> x;
    arr.push_back(x);
  }
  build(1, 0, n - 1);
  long long ans = 0LL;
  for (int i = 0; i < n - 1; i++) {
    ans += query_smaller(1, 0, n - 1, i + 1, n - 1, arr[i] + 1);
  }
  cout << ans << "\n";
  arr.clear();
  for (auto &i : t) {
    i.clear();
  }
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("in.txt", "r", stdin);
  freopen("out1.txt", "w", stdout);
  freopen("error.txt", "w", stderr);
#endif
  ios_base::sync_with_stdio(0); cin.tie(0);
  int t = 1, casee = 1;
  cin >> t;
  while (t--) {
    // cout << "Case #" << casee++ << ": ";
    solve();
  }
  // cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
  return 0;
}