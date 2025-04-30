#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
int main()
{
    struct stat statbuf;
    if (stat("foo", &statbuf) < 0)
        printf("stat error for foo");
    if (chmod("foo", statbuf.st_mode & ~S_IXGRP) < 0)
        printf("chmod error for foo");
    /* set absolute mode to "rw-r--r--" */
    if (chmod("bar", S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH) < 0)
        printf("chmod error for bar");
    exit(0);
}
