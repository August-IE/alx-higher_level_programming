#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - A function that checks if a singly-linked list 
 * 		has a cycle in it
 * @list: A singly-linked list.
 *
 * Return: 0 - if there is no cycle
 *         otherwise 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *light, *dark;

	if (list == NULL || list->next == NULL)
		return (0);

	light = list->next;
	dark = list->next->next;

	while (light && dark && dark->next)
	{
		if (light == dark)
			return (1);

		light = light->next;
		dark = dark->next->next;
	}

	return (0);
}
