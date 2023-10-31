#include "lists.h"

/**
 * check_cycle - to check if a list has a cycle
 * @list: the list
 *
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *static_p = list, *move_p = list;

	if (list == NULL)
		return (0);

	while (static_p != NULL && move_p != NULL && move_p->next != NULL)
	{
		static_p = static_p->next;
		move_p = move_p->next->next;

		if (static_p == move_p)
			return (1);
	}

	return (0);
}

