#include "lists.h"

/**
 * check_cycle - Checks if list has a cycle in it.
 * @list: Singly linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *quick_check = list;
	listint_t *slow_check = list;

	if (list == NULL)
		return (0);
	while ((slow_check != NULL) && (quick_check) && (quick_check->next != NULL))
	{
		slow_check = slow_check->next;
		quick_check = quick_check->next->next;
		if (slow_check == quick_check)
			return (1);
	}
	return (0);
}
