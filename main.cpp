#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    int n, arg2, m;
    string arg1, arg3;
    cin >> n;
    map<string, int> a;
    map<pair<string, string>, int> b;
    for (int i=0; i<n; ++i){
        cin >> arg1 >> arg2;
        a[arg1] = arg2;
    }
    cin >> m;
    for (int i=0; i<m; ++i){
        cin >> arg1 >> arg3;
    }
    
}
