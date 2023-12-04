#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if is palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int values[1000];
	int i = 0, j;

	if (*head == NULL)
		return (1);
	/* Store values of the linked list in an array */
	while (current != NULL)
	{
		values[i] = current->n;
		current = current->next;
	}
	/* Check if the values from a palindrome */
	for (j = 0; j < i / 2; j++)
	{
		if (values[i] != values[i - 1 - j])
			return (0);
	}
	return (1);
}
