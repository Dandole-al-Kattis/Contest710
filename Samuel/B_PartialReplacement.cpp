#include<bits/stdc++.h>
using std::vector;
using std::string;
using std::cin;
using std::cout;

int main(){
    long long testcases;
    cin >> testcases;

    for(long long t = 0; t < testcases; t++){
        long long n, k; 
        cin >> n >> k;

        string s;
        cin >> s;

        int counter = 0;
        int i = 0;
        while (i < s.size()){
            if(s[i] == '*'){
                counter = 1;
                break;
            }
            else
            {
                i++;
            }
        }
        int j = 1;
        int best = -1;
        while(j <= k && i+j < s.size()){
            if(s[i+j] == '*'){
                best = j;
            }
            if(j == k && best != -1){
                i = i+best;
                j = 1;
                best = -1;
                counter++;
            }
            else
            {
                j++;
            }
        }
        if(best != -1){
            counter++;
        }
        cout << counter << "\n";
    }
    return 0;
}