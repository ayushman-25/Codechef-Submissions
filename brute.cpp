/*

* Author : Ayushman Chahar
* About  : IT, Senior

*/

#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <vector>

using namespace std;

typedef long long int ll;

template<typename T, typename U> inline void amin(T &x, U y) {if (y < x) x = y;}
template<typename T, typename U> inline void amax(T &x, U y) {if (x < y) x = y;}

void solve() {
	int n; cin >> n;
	vector<int> arr(n);
	for (int &i : arr) {
		cin >> i;
	}
	int sm = 0;
	for (int i : arr) {
		sm += i;
	}
	cout << sm << "\n";
}

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  int t = 1, casee = 1;
  // cin >> t;
  while (t--) {
    // cout << "Case #" << casee++ << ": ";
    solve();
  }
  // cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
  return 0;
}