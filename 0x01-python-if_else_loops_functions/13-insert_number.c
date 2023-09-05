#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: list to be inserted in
 * @number: value of the node to be inserted
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *o_ptr;
	listint_t *node = malloc(sizeof(listint_t));

	if (node == NULL)
	{
		free(node);
		return (NULL);
	}
	node->n = number;
	if (*head == NULL || node->n < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	ptr = *head;
	o_ptr = ptr->next;
	while (o_ptr != NULL)
	{
		if (node->n >= ptr->n && node->n < o_ptr->n)
		{
			ptr->next = node;
			node->next = o_ptr;
			return (node);
		}
		ptr = o_ptr;
		o_ptr = ptr->next;
	}
	ptr->next = node;
	return (node);
}
