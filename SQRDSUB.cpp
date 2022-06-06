#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    //ios_base :: sync_with_stdio(false);
    //cin.tie(nullptr);
    //cout.tie(nullptr);
    ll t;
    scanf("%lld", &t);
    while(t--) {
        ll n;
        scanf("%lld", &n);
        ll arr[n];
        //ll cnteven = 0;
        for(int i = 0; i < n; i++) {
            scanf("%lld", &arr[i]);
            //if((arr[i] % 2 == 0) || (arr[i] == 0)); cnteven++;
        }
        vector<ll> indexes;//(cnteven);
        vector<ll> elements;//(cnteven);
        for(int i = 0; i < n; i++) {
            if(arr[i] % 2 == 0 || arr[i] == 0) {
                elements.push_back(arr[i]);
                indexes.push_back(i);
            }
        }
        ll TOTAL = (n * (n + 1) / 2);
        ll cnt = 0;
        if(indexes.size() == 0) printf("%lld\n", TOTAL);
        else if(indexes.size() == 1) {
            if((elements[0] != 0) && ((elements[0] / 2) & 1)) {
                if((indexes[0] == 0) || (indexes[0] == n - 1)) cnt += n;
                else cnt += ((indexes[0] + 1) * (n - indexes[0]));
            }
            printf("%lld\n", TOTAL - cnt);
        }
        else {
            for(int i = 0; i < indexes.size(); i++) {
                if(elements[i] != 0 && ((elements[i] / 2) & 1)) {
                    if(i == 0) {
                        ll lh = indexes[i] - 0;
                        ll rh = indexes[i + 1] - indexes[i];
                        ll total = lh + rh;
                        cnt += ((lh + 1) * (total - lh));
                    } else if(i == indexes.size() - 1) {
                        ll lh = indexes[i] - indexes[i - 1];
                        ll rh = n - 1 - indexes[i];
                        ll total = lh + rh;
                        cnt += ((lh) * (total - lh + 1));
                    } else {
                        ll lh = indexes[i] - indexes[i - 1] - 1;
                        ll rh = indexes[i + 1] - indexes[i] - 1;
                        ll total = lh + rh + 1;
                        if((total & 1) && (total / 2 == lh)) cnt += ((lh + 1) * (lh + 1));
                        else cnt += ((lh + 1) * (total - lh));
                    }
                }
            }
            printf("%lld\n", TOTAL - cnt);
        }
    }
    return 0;
}