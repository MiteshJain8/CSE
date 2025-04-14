#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char *argv[])
{
    if (argc == 3)
    {
        printf("Hard linking %s and %s\n", argv[1], argv[2]);
        if (link(argv[1], argv[2]) == 0)
            printf("Hard link created successfully.\n");
        else
            printf("Error creating hard link");
    }
    else if (argc == 4)
    {
        printf("Soft linking %s and %s\n", argv[1], argv[2]);
        if (symlink(argv[1], argv[2]) == 0)
            printf("Soft link created successfully.\n");
        else
            printf("Error creating soft link");
    }

    return 0;
}
