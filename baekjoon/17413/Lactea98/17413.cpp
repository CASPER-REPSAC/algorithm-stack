#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

int main(){
    string input, tmp;
    int start = 0;
    int i = 0;
    bool check = false;

    getline(cin, input);

    for(; i<input.length(); i++){
        if(input[i] == '<') check = true;
        else if(input[i] == '>') check = false;
        else if(check == false){
            for(; i<input.length(); i++){
                if(input[i] == '<') break;
                else if(input[i] == ' '){
                    tmp = input.substr(start, i-start);
                    reverse(tmp.begin(), tmp.end());

                    cout << tmp << " ";
                    start = i + 1;
                }
            }
            tmp = input.substr(start, i-start);
            reverse(tmp.begin(), tmp.end());

            cout << tmp << " ";
            start = i + 1;
        }
    }
    // tmp = input.substr(start, i-start);
    // reverse(tmp.begin(), tmp.end());

    // cout << tmp;
    // cout << input[i];
}