/* bof.c */
#include <stdio.h>

int main()
{
	char buf[100];
	setlinebuf(stdout);
	printf("buf = %p\n", buf);
	gets(buf);
	puts(buf);
	return 0;
}
