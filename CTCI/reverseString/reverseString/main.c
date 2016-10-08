//
//  main.c
//  reverseString
//
//  Created by Jonathan Mares on 1/10/15.
//  Copyright (c) 2015 Mares & Co. All rights reserved.
//

#include <stdio.h>
//Requires a string
void reverse(char * str) {
    //find the last index of the string
    int last = strlen(str)-1;
    printf("length of string is: %d\n",last);
    int first = 0;
   
    while (first<last && first!=last) {
        
        char temp = str[first];
        str[first] = str[last];
        str[last] = temp;
        last--;
        first++;
    
    }
}




int main(int argc, const char * argv[]) {
    char string[] = "hello";
    reverse(&string[0]);
    printf("%s\n",&string[0]);
   
    return 0;
}
