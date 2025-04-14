#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

int main()
{
    int fd = open("test.txt", O_RDWR);
    if (fd == -1)
    {
        perror("open");
        return 1;
    }
    pid_t pid = fork();
    if (pid == -1)
    {
        perror("fork");
        return 1;
    }
    else if (pid == 0)
    {
        char buffer[10];
        read(fd, buffer, 5);
        buffer[5] = '\0';
        printf("Child read: %s\n", buffer);
    }
    else
    {
        wait(NULL);
        char buffer[10];
        read(fd, buffer, 5);
        buffer[5] = '\0';
        printf("Parent read: %s\n", buffer);
    }
    close(fd);
    return 0;
}
