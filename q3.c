#include <stdio.h>

int summer(int num){
    if(num == 0){
        return 0;
    }
    return num%10+ summer(num/10);
}

int main()
{
    printf("%d ",summer(2347623));
    return 0;
}