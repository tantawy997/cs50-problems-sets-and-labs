#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[1])
{
    if (argc != 2)
    {
        printf("Usage: Usage: ./recover IMAGE\n");
        return 1;
    }
    // open memory card
    typedef uint8_t BYTE;
    BYTE memory[512];
    // intilize some  variables we will need later
    const int BLOCK_SIZE = 512;
    int counter = 0;
    char image[8];
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("file could not open \n");
        return 1;
    }
    FILE *img = NULL;
    // a while loop to loop over the file we want to read the data from
    while (fread(&memory, sizeof(BYTE), BLOCK_SIZE, file) != 0)
    {
        // if condition to check for the first 4 bytes to mtach them with the well known to be mostly the first four bytes of every jpeg file
        if (memory[0] == 0xff && memory[1] == 0xd8 && memory[2] == 0xff && (memory[3] & 0xf0) == 0xe0)
        {
            if (counter == 0)
            {
                sprintf(image, "%03i.jpg", counter);
                img = fopen(image, "w");
                fwrite(&memory, sizeof(BYTE), BLOCK_SIZE, img);
                counter++;
            }

            else
            {
                sprintf(image, "%03i.jpg", counter);
                img = fopen(image, "w");
                fwrite(&memory, sizeof(BYTE), BLOCK_SIZE, img);
                counter++;
            }

        }
        else if (counter != 0)
        {
            fwrite(&memory, sizeof(BYTE), BLOCK_SIZE, img);
        }
    }
    fclose(img);
    fclose(file);
    return 0;
}