#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll cnt(ll n)  {  
    n = n - ((n >> 1) & 0x55555555);
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333);
    ll c;
    c = ((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) >> 24;
    return c;

}

int main() {
	ios :: sync_with_stdio(0);
	cin.tie(0);
	ll n;
	cin >> n;
	cout << cnt(n);
	return 0;
}