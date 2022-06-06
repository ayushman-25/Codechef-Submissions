#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	string s1, s2; cin >> s1 >> s2;
	vector<char> v1(s1.begin(), s1.end());
	vector<char> v2(s2.begin(), s2.end());
	sort(s2.begin(), s2.end());
	int n = (int) s1.size();
	for (int i = 0; i < n; i++) {
		vector<char> check;
		for (int j = i; j < n; j++) {
			check.push_back(s1[j]);
			sort(check.begin(), check.end());
			if (equal(check.begin(), check.end(), s2.begin())) {
				cout << j + 1 << "\n";
				break;
			}
		}
	}
}