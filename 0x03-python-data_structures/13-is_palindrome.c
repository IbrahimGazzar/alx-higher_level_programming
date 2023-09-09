#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverseList - reverses the list
 * @head: point to start reversing from
 *
 * Return: head of the reversed list
 */
listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL;
	listint_t *crnt = head;

	while (crnt != NULL)
	{
		next = crnt->next;
		crnt->next = prev;
		prev = crnt;
		crnt = next;
	}
	return (prev);
}
/**
 * is_palindrome - checks if a linked list is a palindrome or not
 * @head: list to be checked
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *s_ptr = *head, *e_ptr = *head;
	listint_t *half = NULL;

	if (head == NULL)
		return (1);
	while (e_ptr != NULL && e_ptr->next != NULL)
	{
		s_ptr = s_ptr->next;
		e_ptr = e_ptr->next->next;
	}
	half = reverseList(s_ptr);
	while (half != NULL)
	{
		if((*head)->n != half->n)
			return (0);
		*head = (*head)->next;
		half = half->next;
	}
	return (1);
}
