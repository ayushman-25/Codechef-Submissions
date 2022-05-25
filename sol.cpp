#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        long long x, y;
        cin >> x >> y;
        if(__gcd(x, y) != 1) {
            cout << "IMPOSSIBLE" << "\n";
        } else {
            cout << (x * y) - x - y + 1 << "\n";
        }
    }
    return 0;
}