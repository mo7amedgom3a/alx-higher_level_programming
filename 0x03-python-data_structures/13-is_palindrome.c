#include "lists.h"
/**
 * is_palindrome - check is a linked list is palindrome
 * @head: head of the list
 * Return: 0 if not 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = (*head);
	listint_t *fast = (*head);
	listint_t *tmp = (*head);
	int count = 0, i;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		count++;
		fast = fast->next->next;
	}
	listint_t *arr = malloc(count * sizeof(listint_t *));

	for (i = 0; i < count; i++)
	{
		arr[i] = *tmp;
		tmp = tmp->next;
	}
	i--;
	while (slow != NULL)
	{
		if (arr[i].n != slow->n)
			return (0);
		slow = slow->next;
		i--;
	}
	return (1);
}
