#include <unistd.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>

int main(int argc, char *argv[])
{
    if (argc != 2){
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    struct stat fileStat;

    if (lstat(argv[1], &fileStat) < 0)
        return 1;
    
    printf("File Name: %s\n", argv[1]);
    printf("File Size: %lu bytes\n", fileStat.st_size);
    printf("Number of hard Links: %lu\n", fileStat.st_nlink);
    printf("File inode: %lu\n", fileStat.st_ino);
    printf("File Permissions: %o\n", fileStat.st_mode);
    printf("Last Access Time: %s", ctime(&fileStat.st_atime));
    printf("Last Modification Time: %s", ctime(&fileStat.st_mtime));

    return 0;
}
