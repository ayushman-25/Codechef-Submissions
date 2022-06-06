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

vector<vector<int>> ans;

// REFERENCES - GFG
void check(vector<int> arr, int ind, vector<int> sub, int myXor, int k) {
	if(ind == arr.size()) {
		if(k == sub.size()) {
			int xorr = 0;
			for(int i: sub) {
				xorr ^= i;
			}
			if(xorr == myXor) {
				ans.emplace_back(sub);
			}
		}
	} else {
		check(arr, ind + 1, sub, myXor, k);
		sub.emplace_back(arr[ind]);
		check(arr, ind + 1, sub, myXor, k);
	}
}

void solve() {
	int n, k;
	cin >> n >> k;
	if(k == 1) {
		cout << n << "\n";
		return;
	}
	int maxXor = ((1 << ((int)log2(n) + 1)) - 1);
	vector<int> myVec, sub;
	for(int i = 1; i <= n; i++) {
		myVec.emplace_back(i);
	}
	check(myVec, 0, sub, maxXor, k);
	for(auto i: ans) {
		sort(i.begin(), i.end());
		for(int z = 0; z < k; z++) {
			cout << i[z] << " \n"[z + 1 == k];
		}
		ans.clear();
		return;
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
    cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    return 0;
}