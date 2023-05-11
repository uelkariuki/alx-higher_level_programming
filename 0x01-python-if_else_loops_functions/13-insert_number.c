#include "lists.h"

/**
 *insert_node- function that inserts a number into a sorted singly linked list.
 *@head: pointer to a pointer to head of the lined list
 *@number: the number to be inserted
 *Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node =  *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	/*insert at end*/
	new_node->n = number;
	new_node->next = NULL;

	/*insert at beginning*/
	if (current_node == NULL || current_node->n >= number)
	{
		new_node->next = current_node;
		*head = new_node;
	}

	/*look for its right position*/
	else
	{
		while (current_node->next && current_node->next->n <= number)
		{
			current_node = current_node->next;
		}
		new_node->next = current_node->next;
		current_node->next = new_node;
	}

	return (new_node);
}
