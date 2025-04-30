#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
int main(void)
{
    pid_t pid, pid1, pid2;
    printf("Parent process started. PID: %d\n", getpid());
    if ((pid = fork()) < 0)
    {
        printf("fork error");
    }
    else if (pid == 0)
    {
        if ((pid1 = fork()) < 0)
            printf("fork error");
        else if (pid1 == 0)
        {
            sleep(5);
            printf("Second child pid: %d\n", getpid());
            printf("second child, parent pid = %ld\n", (long)getppid());
            exit(0);
        }
        else
        {
            printf("First child pid: %d\n", getpid());
            exit(0);
        }
    }
    if ((pid2 = waitpid(pid, NULL, 0)) != pid)
        printf("waitpid error");
    printf("terminated child's pid: %d\n", pid2);
    exit(0);
}
