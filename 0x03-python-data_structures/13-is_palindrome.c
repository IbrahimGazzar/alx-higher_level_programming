#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome or not
 * @head: list to be checked
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *s_ptr = *head, *e_ptr = *head;
	int i, k, len = 0;

	if (head == NULL || *head == NULL)
		return (1);
	while (e_ptr != NULL)
	{
		len++;
		e_ptr = e_ptr->next;
	}
	for (i = 0; i <= (len - 1) / 2; i++)
	{
		e_ptr = *head;
		for (k = len - i - 1; k > 0; k--)
		{
			e_ptr = e_ptr->next;
		}
		if (s_ptr->n != e_ptr->n)
			return (0);
		s_ptr = s_ptr->next;
	}
	return (1);
}
