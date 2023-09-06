#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i;
	listint_t *node;

	i = *head;
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	node->n = number;
	node->next = NULL;
	if (*head == NULL || (*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (i->next != NULL)
	{
		if (i->next->n >= node->n)
		{
			node->next = i->next;
			i->next = node;
			return (node);
		}
		i = i->next;
	}
	i->next = node;
	return (node);
}
