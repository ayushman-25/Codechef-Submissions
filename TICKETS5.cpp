#include <iostream>
#include<bits/stdc++.h>
#include<string.h>
#include <cstdlib>
#include <sstream>  
#include <vector>
#include <set>
#define fio ios_base::sync_with_stdio(false); cin.tie(NULL);
#define mlim 10000000
#define br break
#define pub push_back
#define pi 3.14159265358979323846
#define pob pop_back
#define pf pop_front
#define cc continue
#define ll long long int
#define vl vector<long long int>
#define pll pair<long long int,long long int>
#define sl set<long long int>
 
using namespace std;
string lucky(string s)
{
    if(s[0]==s[1])
    return "NO";
    for(ll i=0;i<s.size()-2;i++)
    {
        if(s[i]!=s[i+2])
        return "NO";
    }    
    return "YES";
}
int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	ll t;
	string s;
	cin>>t;
	while(t--)
	{
	   cin>>s;
	   //cout<<s.size();
	   cout<<lucky(s)<<"\n";
    }
	return 0;
}