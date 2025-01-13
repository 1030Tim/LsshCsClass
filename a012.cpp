#include<iostream>
using namespace std;
int main(){
    long long a,b;
    cin >> a >> b;
    cout << abs(min(a,b)-max(a,b)) << endl;
    return 0;
}