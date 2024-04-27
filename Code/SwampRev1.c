#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
int main(void)
{
    size_t sVar1;
    long lVar2;
    unsigned char local_38[48];

    printf("Please enter the flag:");
    __isoc99_scanf("%33s", local_38);
    sVar1 = strlen((char *)local_38);
    if (sVar1 == 0x20)
    {

        lVar2 = 0;
        while (local_38[lVar2] == ((&DAT_00402047)[lVar2] ^ 0x41))
        {
            puts("test");
            lVar2 = lVar2 + 1;
            if (lVar2 == 0x20)
            {
                puts("Congratulations! You found the flag!");
                return 0;
            }
        }
    }
    puts("The flag entered is incorrect!");
    /* WARNING: Subroutine does not return */
    exit(0);
}