#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list head
 * Return: 0 if no, 1 if yes
 */

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	listint_t *i = list->next;

	while (1)
	{
		if ( i->next == NULL)
			return (0);
		else if (i->next == list)
			return (1);
		i = i->next;
	}
	return (0);
}
