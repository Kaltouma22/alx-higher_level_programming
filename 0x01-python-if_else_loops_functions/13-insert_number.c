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
	listint_t *h = *head;
	listint_t *new_node = create_new_node(number);

	if (new_node == NULL)
		return (NULL);
	if (*head == NULL || (*head)->data >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (h->next != NULL && h->next->data < number)
		{
			h = ->next;
		}
		new_node->next = h->next;
		h->next = new_node;
	}
	return (new_node);
}
