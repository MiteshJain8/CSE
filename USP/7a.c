#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
int main()
{
    int st;
    pid_t pid1 = fork();
    pid_t pid2 = fork();
    if (pid1 == 0)
    {
        printf("first pid:%d\n", getpid());
        sleep(2);
        exit(0);
    }
    if (pid2 == 0)
    {
        printf("second pid:%d\n", getpid());
        sleep(4);
        exit(0);
    }
    wait(&st);
    printf("first wait\n");
    sleep(1);
    waitpid(pid2, &st, 0);
    printf("second wait\n");
    return 0;
}
