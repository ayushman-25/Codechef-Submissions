/*

*  Author : Ayushman Chahar   #
*  About  : IT Sophomore      #
*  Insti  : VIT, Vellore      #

*/

// #pragma GCC optimize "trapv"
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

// References - https://codeforces.com/blog/entry/21853
struct HASH{
      size_t operator()(const pair<int,int>&x)const {
        return hash<long long>()(((long long)x.first)^(((long long)x.second)<<32));
      }
};

int check_arr[(int)1e6 + 1] = {};
unordered_map<pair<int, int>, int, HASH> mymap;
// map<pair<int, int>, int> mymap;

int ans(int m) {
    int games_won = 0;
    for(int i = 1; i <= m; i++) {
        check_arr[i] += check_arr[i - 1];
        amax(games_won, check_arr[i]);
    }
    return games_won;
}

void clear_global() {
    fill(check_arr, check_arr + (int)1e6, 0);
    mymap.clear();
}

void checks(int l, int r, int m, vector<int> arr) {
    check_arr[arr[l]]++;
    check_arr[m + 1]--;
    if (arr[r] <= m) {
        mymap[{arr[l], arr[r]}]++;
        return;
    }
    if (arr[r] > m && arr[l] <= m) {
        return;
    }
    assert(false);
}

void find_eff(int m) {
    for(auto z: mymap) {
        int val = z.first.second + (z.first.first << 1);
        check_arr[z.first.second + z.first.first] -= z.second;
        check_arr[z.first.second + (z.first.first << 1)] += z.second;
        while (val + z.first.second <= m) {
            check_arr[val + z.first.first + z.first.second] += z.second;
            check_arr[val + z.first.second] -= z.second;
            val += (z.first.first + z.first.second);
        }
    }
}

void solve() {
    int n, q, m;
    cin >> n >> q >> m;
    vector<int> arr(n);
    for(int &inp: arr) cin >> inp;
    while(q--) {
        int l, r;
        cin >> l >> r;
        if(arr[--l] > m) {
            continue;
        }
        checks(l, --r, m, arr);
    }
    find_eff(m);
    cout << ans(m) << "\n";
    clear_global();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    mymap.reserve(262144);
    mymap.max_load_factor(0.25);
    int t = 1, casee = 1;
    cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    return 0;
}