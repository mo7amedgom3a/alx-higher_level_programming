#include "lists.h"
/**
 * reverseList - reverse the linked list
 * @head: head of the list
 * Return: reverse the second half of the linked list.
 */

listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - check is a linked list is palindrome
 * @head: head of the list
 * Return: 0 if not 1 if it is
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *secondHalf = reverseList(slow->next);
	listint_t *firstHalf = *head;

	while (secondHalf != NULL)
	{
		if (firstHalf->n != secondHalf->n)
		{
			return (0);
		}
		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}

	return (1);
}
