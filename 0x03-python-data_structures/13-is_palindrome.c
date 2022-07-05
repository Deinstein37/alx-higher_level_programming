#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: the head node passed to us
 *
 * Return: 0 if not, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	short i, j;
	short count = 0;
	int array[3000];

	if (!head || !(*head) || (*head)->next == NULL)
		return (1);
	while (*head)
	{
		array[count] = (*head)->n;
		*head = (*head)->next;
		count++;
	}
	for (i = 0, j = count - 1; i < count / 2 + 1; i++, j--)
		if (array[i] != array[j])
			return (0);
	return (1);
}
