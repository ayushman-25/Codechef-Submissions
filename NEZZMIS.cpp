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

vector<ll> initializeDiffArray(vector<ll>& A, int n) { 
    vector<ll> D(n + 2); 
    D[0] = A[0], D[n] = 0; 
    for (int i = 1; i < n; i++) D[i] = A[i] - A[i - 1]; 
    return D; 
} 

void update(vector<ll>& D, int l, int r, ll x) { 
    D[l] += x; D[r + 1] -= x; 
} 


void solve() {  
    int n, q;
    cin >> n;
    vector<ll> arr(n); for(ll& inp: arr) cin >> inp; 
    cin >> q;
    vector<ll> D = initializeDiffArray(arr, n);
    while(q--) {
        string check;
        cin >> check;
        if(check != "U") {
            int l = stoi(check), r;
            ll val;
            cin >> r >> val;
            l--; r--;
            update(D, l, r, val);
        } else {
            for(int i = 0; i < n; i++) {
                if (i == 0)  arr[i] = D[i];  
                else arr[i] = D[i] + arr[i - 1]; 
                cout << arr[i] << " "; 
            }
            cout << "\n";
        }
    }
}

int main() {
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