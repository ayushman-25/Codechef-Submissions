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

const int N = 1e6;
vector<int> primes(N, 1);
vector<int> dp = {0};

void seive() {
	primes[0] = primes[1] = 0;
	int p = 2;
	while(p * p <= N + 1) {
		if(primes[p]) {
			for(int i = p * p; i <= N; i += p) {
				primes[i] = 0;
			}
		}
		p++;
	}
}

void pre_compute() {
	for(int i = 1; i <= N; i++) {
		dp.emplace_back(dp.back() + primes[i]);
	}
}

void solve() {
	int x, y;
	cin >> x >> y;
	cout << (dp[x] > y ? "Divyam\n" : "Chef\n");
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

 	seive();
 	pre_compute();

    int t = 1, casee = 1;
    cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    return 0;
}