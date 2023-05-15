#include "lists.h"

/**
 * is_palindrome- function in C that checks if a singly linked
 *                list is a palindrome
 * @head: a pointer to a pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *hare = *head, *tortoise = *head, *previous, *right, *left;
	listint_t *next = NULL, *current;

	if (*head == NULL)
		return (1);
	while (hare != NULL && hare->next != NULL) /*find midpoint of list*/
	{
		hare = hare->next->next;
		tortoise = tortoise->next;
	}
	previous = NULL; /*reverse second half of the list*/
	current = tortoise;
	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	left = *head; /* comapare the first half and the second*/
	right = previous; /*half that was reversed*/
	while (right != NULL)
	{
		if (right->n != left->n)
			return (0);
		right = right->next;
		left = left->next;
	}
	previous = NULL; /* restore like it was previously before reversing*/
	current = previous;
	next = NULL;
	while (right != NULL)
	{
		next = right->next;
		right->next = current;
		current = right;
		right = next;
	}
	tortoise->next = current;
	return (1);
}
