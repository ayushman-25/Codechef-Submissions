#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int t;
	cin >> t;
	while(t--) {
		ll n, d;
		string po;
		cin >> n;
		cin >> po;
		cin >> d;
		vector<char> pop;
		for(int i = 0; i < n; i++) {
			pop.push_back(po[i]);
		} 
		vector<int> dl(d);
		for(auto& i1: dl) cin >> i1;
		vector<char> status(n, 'N');
		//memset(&status[0], 'N', sizeof(status[0]) * status.size());  
		for(int i = 0; i < d; i++) {
			status[i - 1] = 'I';
			if(pop[0] == '1' && status[1] == 'N') pop[1] = '1';
			vector<int> temp;
			for(int j = 0 ; j < n; j++) {
				if(pop[j] == '1') temp.push_back(j);
			}
			for(int j = 0; j < temp.size(); j++) {
				if(pop[temp[j]] == '1') {
					if(status[temp[j]] == 'N') pop[temp[j] - 1] = '1';
					if(status[temp[j] + 1] == 'N') pop[temp[j] + 1] = '1';
				}	
			}
			if(pop[-1] == '1' && status[-1] == 'N') pop[-2] = '1'; 
		}
		cout << count(pop.begin(), pop.end(), '1') << "\n";
	} 
	return 0;
}