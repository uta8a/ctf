/* fsb.c */
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
	char buf[100];
	printf("[+] buf = %p\n", buf);
	strncpy(buf, argv[1], 100);
	printf(buf);
	putchar('\n');
	return 0;
}
