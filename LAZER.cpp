#include<bits/stdc++.h>
#define ll long long
using namespace std;

struct Point {
	ll x;
	ll y;
};

bool onSegment(Point p, Point q, Point r) {
	if(q.x <= max(p.x, r.x) && q.x >= min(p.x, r.x) && q.y <= max(p.y, r.y) && q.y >= min(p.y, r.y))
		return true;
	return false;
}

int orientation(Point p, Point q, Point r) {
	int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
	if(val == 0) return 0;
	return(val > 0) ? 1: 2;
}

bool doIntersect(Point p1, Point q1, Point p2, Point q2) {
	int o1 = orientation(p1, q1, p2);4
	int o2 = orientation(p1, q1, q2);
	int o3 = orientation(p2, q2, p1);
	int o4 = orientation(p2, q2, q1);

	if(o1 != o2 && o3 != o4)
		return true;
	if(o1 == 0 && onSegment(p1, p2, q1))
		return true;
	if(o2 == 0 && onSegment(p1, q2, q1))
		return true;
	if(o3 == 0 && onSegment(p2, p1, q2))
		return true;
	if(o4 == 0 && onSegment(p2, q1, q2))
		return true;
	return false;
}


int main() {
	ios_base :: sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	while(t--) {
		ll n, q;
		cin >> n >> q;
		ll arr1[n];
		for(int i = 0; i < n; ++i) cin >> arr1[i];
		for(int j = 0; j < q; ++j) {
			ll x1, x2, y, cnt = 0;
			cin >> x1 >> x2 >> y;
			struct Point p1 = {x1, y}, q1 = {x2, y};
			for(int k = 0; k < n - 1; k++) {
				struct Point p2 = {k + 1, arr1[k]}, q2 = {k + 2, arr1[k + 1]};
				if(doIntersect(p1, q1 ,p2, q2)) cnt++;
				if((k + 2 == x1 && arr1[k + 1] == y) || (k + 1 == x2 && arr1[k] == y)) cnt--;
			}
			cout << cnt << "\n";
		}
	}
	return 0;
}