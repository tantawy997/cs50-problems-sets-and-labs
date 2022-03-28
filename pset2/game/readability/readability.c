#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>


int main(void)

// this function is to calculate the grade of each text the user provide to us
{
    // prompt the user to input text

    string text = get_string("text: ");

    int letter = 0;
    int word = 1;
    int sentence = 0;

    {
        // a for loop to itatrate over the test to calculate each number of the letter and words and sentence in the text
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
    // computing the Coleman-Liau index by providing it the word & letter & sentence varaiables

    float grade = round(0.0588 * (100 * letter / (float)word) - 0.296 * (100 * sentence / (float)word) - 15.8);

    {
        if (grade < 1)

        {
            printf("Before Grade 1\n");
        }
        else if (grade >= 16)

        {
            printf("Grade 16+\n");

        }
        else
        {
            printf("Grade %.f\n", grade);
        }
    }

}


