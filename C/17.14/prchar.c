#include <stdio.h>

void print_chars(char *s, int len){
    int n = 0;
    while (n < len){
        printf("%2x ", (unsigned char) s[n]);
        n++;
    }
    printf("\n");
}


