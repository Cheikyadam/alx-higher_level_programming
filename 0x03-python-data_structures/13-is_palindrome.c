#include "lists.h"
#include <stddef.h>

/**
 * list_lenght - len of a list
 * @l: the list
 *
 * Return: the lenght
 */

int list_lenght(listint_t *l)
{
	listint_t *mov = l;
	int len = 0;

	while (mov != NULL)
	{
		len++;
		mov = mov->next;
	}
	return (len);
}

/**
 * el_at_index - to find the element at a given index
 * @list: the list
 * @idx: the index
 *
 * Return: the element
 */

int el_at_index(listint_t *list, int idx)
{
	int i = 1;
	listint_t *mov = list;

	while (mov != NULL)
	{
		if (i == idx)
		{
			return (mov->n);
		}
		i++;
		mov = mov->next;
	}
	return (-1);
}

/**
 * is_palindrome - palindrome with list
 * @head: the list
 *
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	int index = 1, len = 0;
	listint_t *mov = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	len = list_lenght((*head));
	while (mov != NULL)
	{
		if (mov->n == el_at_index((*head), len))
		{
			mov = mov->next;
			len--;
			index++;
		}
		else
		{
			return (0);
		}
	}
	return (1);
}
