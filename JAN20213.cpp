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

int getSum(int BITree[], int index) { 
    int sum = 0;
    index = index + 1; 
    while (index>0) { 
        sum += BITree[index]; 
        index -= index & (-index); 
    } 
    return sum; 
}

void updateBIT(int BITree[], int n, int index, int val) { 
    index = index + 1; 
    while (index <= n) { 
        BITree[index] += val; 
        index += index & (-index); 
    }    
}

int *constructBITree(vector<int> arr, int n) { 
    int *BITree = new int[n+1]; 
    for (int i=1; i<=n; i++) 
        BITree[i] = 0; 
    for (int i=0; i<n; i++) 
        updateBIT(BITree, n, i, arr[i]); 
    return BITree; 
}

void solve() {
    int n, q;
    cin >> n;
    vector<int> my;
    for(int i = 1; i <= n; i++) {
        int ub = 0;
        int val = i;
        while(val) {
            if((val & 1) == 0) ub++;
            val >>= 1;
        }
        my.push_back(1 << ub);
    }
    int *BITree = constructBITree(my, n);
    cin >> q;
    while(q--) {
        int l, r;
        cin >> l >> r;
        if(l == 1) {
            cout << getSum(BITree, r - 1) << "\n";
        } else {
            cout << getSum(BITree, r - 1) - getSum(BITree, l - 2) << "\n";
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