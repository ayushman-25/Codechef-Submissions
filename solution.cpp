#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

const ll M = 1e9+7;

ll fact(ll n) {
    if(n <= 1) return 1;
    return (n % M * fact(n-1) % M) % M;
}

ll solve() {
   string word; cin>>word;
   ll n = word.length();
   unordered_map<char,int> mp;
   for(ll i=0; i<n; i++) {
       mp[word[i]]++;
   }
   ll ans = fact(n);
   for(auto itr = mp.begin(); itr != mp.end(); itr++) {
       ans = ans/fact(itr->second);
   }
   return ans;
}

int main() 
{   
    ios::sync_with_stdio(0);
    cin.tie(0);
	int t = 1;
	// cin>>t;
	
	while(t--) cout<<solve()<<'\n';
	
	return 0;
}