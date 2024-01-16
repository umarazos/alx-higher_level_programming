#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: Node pointing to the head
 * Return: 1 if linked in cycle,
 * 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *storage, *current;

	current = list;
	storage = current;

	while (current != NULL)
	{
		if (current->next == storage)
		{
			return (1);
		}
		current = current->next;
	}
	return (0);
}
