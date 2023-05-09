#include "lists.h"

/**
 * check_cycle- function that checks if a singly linked list has a cycle in it
 * @list: the list to be traversed
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list, *tortoise = list;

	while (hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (hare == tortoise)
		{
			return (1);
		}
	}
	return (0);
}

