#include <stdio.h>
#include <string.h>

int pmatch(char *string, char *pat, int *failure)
{
    int i = 0, j = 0;
    int lens = strlen(string);
    int lenp = strlen(pat);
    while (i < lens && j < lenp)
    {
        if (string[i] == pat[j])
        {
            i++;
            j++;
        }
        else if (j == 0)
        {
            i++;
        }
        else
        {
            j = failure[j - 1] + 1;
        }
    }
    return ((j == lenp) ? (i - lenp) : -1);
}

void fail(char *pat, int *failure)
{
    int i, j;
    int lenp = strlen(pat);
    failure[0] = -1;
    for (j = 1; j < lenp; j++)
    {
        i = failure[j - 1];
        if ((pat[j] != pat[i + 1]) && (i >= 0))
            i = failure[i];
        if (pat[j] == pat[i + 1])
            failure[j] = i + 1;
        else
            failure[j] = -1;
    }
}

int main()
{
    char string[1000];
    printf("Enter a string: ");
    scanf("%s", string);
    char pat[1000];
    printf("\nEnter a pattern: ");
    scanf("%s", pat);
    int failure[1000];
    fail(pat, failure);
    int y = pmatch(string, pat, failure);
    printf("\n(KMP)Pattern found at index %d", y);
    return 0;
}