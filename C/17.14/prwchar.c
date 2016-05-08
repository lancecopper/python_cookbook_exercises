#include <stdio.h>
#include "python3.4/Python.h"

void print_wchars(wchar_t *s, int len){
    int n = 0;
    while (n < len){
        printf("%x ", s[n]);
        n++;
    }
    printf("\n");
}


