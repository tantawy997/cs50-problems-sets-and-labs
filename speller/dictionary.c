// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 25;
int dict_size = 0;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // hash word to obtain a hash value
    int hash_value = hash(word);
    // access linked list at that index in a hash table
    node *n = table[hash_value];
    // looking for the word in the dictionary

    while (n != NULL)
    {
        if (strcasecmp(word, n -> word) == 0)
        {
            return true;
        }

        n = n -> next;
        
    }
    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    // TODO: Improve this hash function
    return sum = sum % N;
    return sum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    FILE *first = fopen(dictionary, "r");

    if (first == NULL)
    {
        return false;
    }
    char next_word[LENGTH + 1];

    while (fscanf(first, "%s", next_word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;

        }
        strcpy(n -> word, next_word);
        n -> next = NULL;
        // hash word to obtain next value
        int index = hash(next_word);
        if (table[index] == NULL)
        {
            table[index] = n;
        }
        else
        {
            n-> next = table[index];
            table[index] = n;
        }
        // insert node at that location
        dict_size++;
    }

    // TODO
    fclose(first);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{

    return dict_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i] -> next;
            free(table[i]);
            table[i] = tmp;
        }
    }

    return true;
}
