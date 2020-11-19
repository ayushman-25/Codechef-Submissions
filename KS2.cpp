#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
	ll t;
	cin >> t;
	while(t--) {
		ll n;
		cin >> n;
		ll cnt = 0, start = 19;
		while(true) {
			ll sum = 0; 
    		while (start != 0) { 
     			sum += (start % 10); 
     			start /= 10; 
    		} 
    		if(sum % 10 == 0) cnt++;
    		if(cnt == n) cout << start << "\n"; break;
    		start++;
		}
	}
	return 0;
}