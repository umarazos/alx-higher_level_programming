#include "lists.h"

/**
 * insert_node - Inserts number into a sorted list.
 * @head: A pointer the head of the list.
 * @number: Number to insert to a sorted list.
 *
 * Return: The address of the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *checker = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (checker == NULL || checker->n >= number)
	{
		newNode->next = checker;
		*head = newNode;
		return (newNode);
	}

	while (checker && checker->next && checker->next->n < number)
		checker = checker->next;

	newNode = checker->next;
	checker->next = newNode;

	return (newNode);
}
