#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>



int main(int argc, string argv[])

{
    if (argc != 2)
    {
        printf("usage: ./caesar key \n");
        return 1;
    }
    // checking if one of the arguments isalpha (we need an integer) - Looping through the string of integers
    for (int i = 0; i < strlen(argv[1]); i++)

        if (isalpha(argv[1][i]))
        {
            printf("Usage: ./caesar key \n");
            return 1;
        }

    int key = atoi(argv[1]);
    string plain_text = get_string("plain text: ");

    printf("ciphertext: ");

    for (int k = 0, t = strlen(plain_text); k < t; k++)

    {
        char c = plain_text[k];
        if (isalpha(plain_text[k]))

        {
            if (islower(plain_text[k]))
            {
                printf("%c", (((plain_text[k] + key) - 'a') % 26) + 'a');

            }
            else if (isupper(plain_text[k]))
            {
                printf("%c", (((plain_text[k] + key) - 'A') % 26) + 'A');

            }

        }
        else
                
                
             
        
                    printf("%c", c);
        }
        


    printf("\n");
}