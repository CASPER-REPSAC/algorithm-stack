#include <iostream>
#include <deque>
#include <cstring>

using namespace std;

int main(){
    int num, tmp;
    char command[11];
    deque<int> d;

    scanf("%d", &num);
    while(num--){
        scanf("%s", command);

        if(!strcmp(command, "push_front")){
            scanf("%d", &tmp);
            d.push_front(tmp);
        }
        else if(!strcmp(command, "push_back")){
            scanf("%d", &tmp);
            d.push_back(tmp);
        }
        else if(!strcmp(command, "pop_front")){
            if(d.size() == 0) printf("-1\n");
            else {
                printf("%d\n", d[0]);
                d.pop_front();
            }
        }
        else if(!strcmp(command, "pop_back")){
            if(d.size() == 0) printf("-1\n");
            else {
                printf("%d\n", d[d.size() - 1]);
                d.pop_back();
            }
        }
        else if(!strcmp(command, "size")) printf("%d\n", d.size());
        else if(!strcmp(command, "empty")) printf("%d\n", (d.empty() ? 1 : 0));
        else if(!strcmp(command, "front")){
            if(d.size() == 0) printf("-1\n");
            else printf("%d\n", d[0]);
        }
        else if(!strcmp(command, "back")){
            if(d.size() == 0) printf("-1\n");
            else printf("%d\n", d[d.size() - 1]);
        }
    }
}