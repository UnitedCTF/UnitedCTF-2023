#include <stdio.h>
#include <string.h>
#include <stdint.h>

char* getFirstFlag() {
    return "flag-intro";
}

void getSecondFlag(char *string_flag, char *static_analysis_flag) {
    strncpy(static_analysis_flag, string_flag, 5);
    char reversed_operand[9] = "aureverse";
    for (int i = 0; i < 9; i++) {
        static_analysis_flag[5 + i] = reversed_operand[i];
    }
    static_analysis_flag[14] = '\0';
}

void computeThirdFlag() {
    uint8_t encrypted_flag3[64] = {97, 52, 97, 77, 67, 34, 45, 28, 116, 62, 85, 42, 94, 85, 72, 40, 106, 115, 103, 44, 107, 118, 68, 13, 39, 98, 75, 103, 74, 51, 68, 120, 110, 113, 113, 110, 107, 99, 110, 40, 126, 105, 107, 100, 110, 114, 98, 112, 45, 80, 66, 108, 110, 96, 111, 60, 114, 101, 108, 96, 116, 115, 120, 115}; // flag-engineering
    char key[14] = "drunken-sailor";
    char decrypted_flag3[16];
    for (int i = 0; i < 16; i++) {
        decrypted_flag3[i] = (encrypted_flag3[i + 0 * 16] ^ (key[i % 14])) + (encrypted_flag3[i + 1 * 16] ^ (key[i % 14])) + (encrypted_flag3[i + 2 * 16] ^ (key[i % 14])) + (encrypted_flag3[i + 3 * 16] ^ (key[i % 14]));
    }
    decrypted_flag3[16] = '\0';
    printf("Arrrgg!\n");
}

int main(int argc, char** argv) {
    char *flag1 = getFirstFlag();

    char flag2[14];
    getSecondFlag(flag1, flag2);

    computeThirdFlag();
}