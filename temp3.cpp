#include <bits/stdc++.h>
#define int long long int
using namespace std;

bool decision(bool a, bool b, bool c)
{
    if (a == c)
        return !a;
    else
        return b;
}

signed main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        vector<bool> v;
        int count = 0;
        if (s[n - 1] == 'L')
            v.push_back(0);
        else
            v.push_back(1);
        for (int i = 0; i < n; i++)
        {
            if (s[i] == 'L')
                v.push_back(0);
            else
                v.push_back(1);
        }
        for (int i = 0; i < v.size() - 3; i++)
        {
            if (v[i + 1] == decision(v[i], v[i + 1], v[i + 2]))
                continue;
            else
            {
                v[i + 1] = decision(v[i], v[i + 1], v[i + 2]);
                count++;
            }
        }
        cout << count << endl;
    }

    return 0;
}