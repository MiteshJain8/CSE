#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
int main()
{
    int file = 0, n;
    char buffer[25];
    if ((file = open("test.txt", O_RDONLY)) < -1)
        printf("file open error \n");
    if (read(file, buffer, 20) != 20)
        printf("file read operation failed\n");
    else
        write(STDOUT_FILENO, buffer, 20);
    printf("\n");
    if (lseek(file, 10, SEEK_SET) < 0)
        printf("lseek operation from beginning of file failed\n");
    if (read(file, buffer, 20) != 20)
        printf("file read operation failed\n");
    else
        write(STDOUT_FILENO, buffer, 20);
    printf("\n");

    if (lseek(file, 10, SEEK_CUR) < 0)
        printf("lseek operation from current position of file failed\n");
    if (read(file, buffer, 20) != 20)
        printf("file read operation failed\n");
    else
        write(STDOUT_FILENO, buffer, 20);
    printf("\n");

    if ((n = lseek(file, 0, SEEK_END)) < 0)
        printf("lseek operation to end of file failed\n");
    printf("size of file is %d bytes\n", n);
    close(file);
    return 0;
}
