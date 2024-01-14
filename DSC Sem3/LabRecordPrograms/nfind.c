#include <stdio.h>
#include<string.h>

int nfind(char *string,char *pat)
{
    int i,j,start=0;
    int lasts=strlen(string)-1;
    int lastp=strlen(pat)-1;
    int endmatch; 
    for(endmatch=lastp;endmatch<=lasts;endmatch++,start++)
    {
        if(string[endmatch]==pat[lastp])
            for(j=0,i=start;j<lastp && string[i]==pat[j];i++,j++);
        if(j==lastp)
            return start;
    }
    return -1;
} 

int main(){
    char string[1000];
    printf("Enter a string: ");scanf("%s",string);
    char pat[1000];
    printf("\nEnter a pattern to check if its present in the entered string: ");
    scanf("%s",pat);
    int x = nfind(string,pat);
    printf("\nPattern found at index %d",x);
    return 0;
}