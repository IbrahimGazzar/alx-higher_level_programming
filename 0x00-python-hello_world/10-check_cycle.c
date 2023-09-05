#include "lists.h"

/**
 * check_cycle - checks if a cycle exists in a linked list or not
 * @list: head of the list to be checked
 *
 * Return: 0 if there's no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;

	while(list != NULL)
	{
		ptr = list;
		while (ptr != NULL)
		{
			ptr = ptr->next;
			if (ptr == list)
				return (1);
		}
		list = list->next;
	}
	return (0);
}
