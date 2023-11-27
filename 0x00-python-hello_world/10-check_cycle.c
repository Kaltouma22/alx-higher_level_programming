#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: Pointer to the head of the libnked list
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
