#include<bits/stdc++.h>
using std::vector;
using std::string;
using std::cin;
using std::cout;

int main(){
    long long testcases;
    cin >> testcases;

    for(long long t = 0; t < testcases; t++){
        long long n, m, x; 
        cin >> n >> m >> x;

        long long rows = (x-1)%n;
        long long cols = (x-1)/n;

        // cout << "row :"  << rows << "column :" << cols << "\n";

        long long x_by_cols = ((rows*m) + cols)+1;

        cout << x_by_cols << "\n";
    }
    return 0;
}