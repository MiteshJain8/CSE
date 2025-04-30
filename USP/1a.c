#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int source, dest, n;
    char buf;
    int filesize;
    int i;

    if (argc != 3)
    {
        fprintf(stderr, "usage %s <source> <dest>", argv[0]);
        exit(-1);
    }

    if ((source = open(argv[1], O_RDONLY)) < 0)
    {
        fprintf(stderr, "can't open source\n");
        exit(-1);
    }

    if ((dest = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC)) < 0)
    {
        fprintf(stderr, "can't create dest\n");
        exit(-1);
    }

    filesize = lseek(source, (off_t)0, SEEK_END);
    printf("Source file size is %d\n", filesize);

    for (i = filesize - 1; i >= 0; i--)
    {
        lseek(source, (off_t)i, SEEK_SET);

        if ((n = read(source, &buf, 1)) != 1)
        {
            fprintf(stderr, "can't read 1 byte");
            exit(-1);
        }

        if ((n = write(dest, &buf, 1)) != 1)
        {
            fprintf(stderr, "can't write 1 byte");
            exit(-1);
        }
    }
    write(STDOUT_FILENO, "DONE\n", 5);
    close(source);
    close(dest);

    return 0;
}
