#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node-Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list
 * @number: Number to be inserted
 * Return: the adress of the new node, or Null if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *src = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->data = number;

	if (*head == NULL || number < src->data)
	{
		new_node->next = src;
		*head = new_node;
		return (new_node);
	}
	while (src->next != NULL && number > src->next->data)
	{
		src = src->next;
	}
	new_node->next = src->next;
	src->next = new_node;

	return (new_node);
}
