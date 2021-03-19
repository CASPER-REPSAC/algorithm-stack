#include <iostream>
#include <queue>

using namespace std;

int main(){
    int n, k;
    queue<int> q;

    scanf("%d %d", &n, &k);
    for(int i=1; i<n+1; i++) q.push(i);

    printf("<");
    while(true){
        for(int _ = 0; _ < k-1; _++){
            q.push(q.front());
            q.pop();
        }
        
        if(q.size() == 1){
            printf("%d>\n", q.front());
            break;
        }
        printf("%d, ", q.front());
        q.pop();
    }
}