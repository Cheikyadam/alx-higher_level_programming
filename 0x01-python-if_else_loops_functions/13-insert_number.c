#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserting in a list
 * @head: the lis
 * @number: the number to be inserted
 *
 * Return: the list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *to_add = malloc(sizeof(listint_t));
	listint_t *to_move = *head;

	if (to_add == NULL)
		return (NULL);
	to_add->n = number;
	if ((*head) == NULL || number <= (*head)->n)
	{
		to_add->next = (*head);
		(*head) = to_add;
		return (to_add);
	}
	while (to_move->next != NULL && number >= to_move->next->n)
		to_move = to_move->next;
	if (to_move->next == NULL)
	{
		to_move->next = to_add;
		to_add->next = NULL;
		return (to_add);
	}
	to_add->next = to_move->next;
	to_move->next = to_add;
	return (to_add);
}
