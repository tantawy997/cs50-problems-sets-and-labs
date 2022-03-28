#include "helpers.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {

            double average = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;

            image[i][j].rgbtBlue = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtRed = round(average);


        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);



            image[i][j].rgbtBlue = (sepiaBlue > 255)? 255 : sepiaBlue;
            image[i][j].rgbtGreen = (sepiaGreen > 255)? 255 : sepiaGreen;
            image[i][j].rgbtRed = (sepiaRed > 255)? 255 : sepiaRed;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width /2); j++)
        {
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            int red = image[i][j].rgbtRed;

            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;

            image[i][width - j - 1].rgbtBlue = blue;
            image[i][width - j - 1].rgbtGreen =  green;
            image[i][width - j - 1].rgbtRed = red;





        }
    }
    return;
}

void blur(int height, int width, RGBTRIPLE image[height][width])

{

    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = 0;
            int green = 0;
            int red = 0;
            float counter = 0.0;
            for (int c = -1; c < 2; c++)
            {
                for (int e = -1; e < 2; e++)
                {
                    if (i + c < 0|| i + c > height -1 || j + e < 0 || j + e > width -1)
                    {
                        continue;
                    }

                    blue += image[i + c][j + e].rgbtBlue;
                    green += image[i + c][j + e].rgbtGreen;
                    red += image[i + c][j + e].rgbtRed;
                    counter++;

                }
            }
            copy[i][j].rgbtBlue = round(blue / counter);
            copy[i][j].rgbtGreen = round(green / counter);
            copy[i][j].rgbtRed = round(red / counter);
        }

    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
            image[i][j].rgbtGreen =  copy[i][j].rgbtGreen;
            image[i][j].rgbtRed =  copy[i][j].rgbtRed;
        }
    }



return;
}