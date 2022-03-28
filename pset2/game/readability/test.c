#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>


int main(void)

{

    string text = get_string("text: ");

    int letter = 0;
    int word = 1;
    int sentence = 0;

    {
        for (int i = 0, n = strlen(text); i < n; i++)

        {

            if (isupper(text[i]))

            {
                letter++;
            }
            else if (islower(text[i]))
            {
                letter++;
            }

            if (text[i] ==  ' ')

            {
                word++;
            }
            if (text[i] == ('!') || text[i] == ('?') || text[i] == ('.'))

            {
                sentence++;
            }


        }
    }

    printf("\n");

    float grade = round(0.0588 * (100 * letter / (float)word) - 0.296 * (100 * sentence / (float)word) - 15.8);

    {
        if (grade < 1)

        {
            printf("before grade 1 \n");
        }
        else if (grade >= 16)

        {
            printf("grade is 16+ \n");

        }
        else
        {
            printf("grade is:%.f \n", grade);
        }
    }

}


