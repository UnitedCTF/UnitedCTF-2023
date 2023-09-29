#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void secret() {
  errno = 0;
  FILE *file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Arrrg! The map's missing! %d\n", errno);
    exit(0);
  }
  char flag[100];
  fgets(flag, sizeof(flag), file);
  printf("%s\n", flag);
  fclose(file);
}

void check() {
  char hint[32];
  char is_treasure_found = 0;
  printf("Enter the treasure hint (max 32 characters): ");
  scanf("%33s", hint);

  if (strcmp(hint, "BlackbeardCompass") == 0) {
    printf("That be right!\n");
  } else {
    printf("That ain't it, matey!\n");
  }

  if (is_treasure_found == '!') {
    secret();
  }
}

int main() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);

  check();

  return 0;
}
