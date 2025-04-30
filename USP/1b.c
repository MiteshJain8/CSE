#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

int main() {
	int fd = open("test.txt", O_RDWR);
    if (fd == -1) {
        perror("open");
        exit(1);
    }
    pid_t pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(1);
    } else if (pid == 0) {
        char buf[10];
        read(fd, buf, 5);
        buf[5] = '\0'; 
        printf("Child process read: %s\n", buf);
    } else {
        wait(NULL);
        char buf[10];
        read(fd, buf, 5);
        buf[5] = '\0'; 
        printf("Parent process read: %s\n", buf);
    }
    close(fd);
    return 0;
}