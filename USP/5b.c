#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main() {
    // dup() demonstration
    int fd1 = open("dup_test.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    int fd2 = dup(fd1);
    printf("dup(): Original fd: %d, New fd: %d\n", fd1, fd2);
    write(fd1, "Line from fd1\n", 14);
    write(fd2, "Line from fd2\n", 14);
    close(fd1);
    close(fd2);
    
    // dup2() demonstration
    int fd3 = open("dup2_test.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    int fd4 = 10;  // Specific fd number we want to use
    dup2(fd3, fd4);
    printf("dup2(): Original fd: %d, Specified fd: %d\n", fd3, fd4);
    write(fd3, "Line from fd3\n", 14);
    write(fd4, "Line from fd4\n", 14);
    close(fd3);
    close(fd4);
    
    return 0;
}