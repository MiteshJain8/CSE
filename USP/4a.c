#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <utime.h>
#include <time.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{
    int fd;
    struct stat statbuf_1;
    struct stat statbuf_2;
    struct utimbuf times;

    if (stat(argv[1], &statbuf_1) < 0) /*Destination file status*/
        printf("Error!\n");

    if (stat(argv[2], &statbuf_2) < 0) /* Source file status*/
        printf("Error!\n");

    printf("Before Copying ...\n");
    printf("Access Time %s\nModification Time%s\n", ctime(&statbuf_1.st_atime), ctime(&statbuf_1.st_mtime));

    times.modtime = statbuf_2.st_mtime;
    times.actime = statbuf_2.st_mtime;
    if (utime(argv[1], &times) < 0)
        printf("Error copying time \n");

    if (stat(argv[1], &statbuf_1) < 0)
        printf("Error!\n");

    printf("After Copying ...\n");
    printf("Access Time %s\nModification Time%s\n", ctime(&statbuf_1.st_atime), ctime(&statbuf_1.st_mtime));
    return 0;
}
