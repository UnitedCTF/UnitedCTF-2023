#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>

unsigned int balance = 0x00000fff;
const unsigned int map_cost =
    0xfffffffe;

void show_flag() {
  errno = 0;
  printf("\nYe've obtained the Legendary Treasure Map!\n");
  FILE *file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Arrrg! The map's missing! %d\n", errno);
    exit(0);
  }

  char flag[100];
  fgets(flag, sizeof(flag), file);
  printf("The map reads: %s\n", flag);
  fclose(file);
}

void check_balance() {
  printf("\nYe have %u gold doubloons!\n", balance);
}

void buy_item(unsigned int cost) {
  if (cost > balance && cost != 1) {
    printf("\nYe don't have enough doubloons for that!\n");
  } else {
    if (cost == map_cost) {
      show_flag();
      exit(0);
    }
    printf("\nThank ye for your purchase! Ye have %u doubloons left.\n",
           balance - cost);
    balance -= cost;
  }
}

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
  init();
  int choice;

  printf("Ahoy! Welcome to Captain Redbeard's Treasure Exchange!\n");

  while (1) {
    printf("\nWhat would ye like to do?\n");
    printf("1. Check thy doubloons\n2. Buy a parrot (50 doubloons)\n3. Buy a "
           "ship wheel (20 doubloons)\n4. Buy a rusty old map (1 doubloon)\n5. "
           "Buy the Legendary Treasure Map (It's really expensive, trust "
           "me!)\n6. Leave the exchange\n");
    scanf("%d", &choice);
    getchar(); // Consume newline

    switch (choice) {
    case 1:
      check_balance();
      break;
    case 2:
      buy_item(50); // parrot
      break;
    case 3:
      buy_item(20); // ship wheel
      break;
    case 4:
      buy_item(1); // rusty old map
      break;
    case 5:
      buy_item(map_cost); // Legendary Treasure Map
      break;
    case 6:
      printf("\nMay seas be ever calm for ye! Farewell!\n");
      exit(0);
    default:
      printf("\nThat ain't a choice I recognize!\n");
    }
  }

  return 0;
}

