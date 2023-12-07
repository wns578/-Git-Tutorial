#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct city
{
	char name[50];
	char country[50];
	int population;
}City;

int main()
{
	City arr[3];
	int i;
	printf("Input three cities:\n");
	for (i = 0; i < 3; i++)
	{
		printf("Name> ");
		scanf("%[^\n]s", arr[i].name);
		fgetc(stdin);

		printf("Country> ");
		scanf("%[^\n]s", arr[i].country);
		fgetc(stdin);

		printf("Population> ");
		scanf("%d", &arr[i].population);
		fgetc(stdin);
	}
	for (i = 0; i < 3; i++)
		printf("%d. %s in %s with a population of %d people \n", i+1, arr[i].name, arr[i].country, arr[i].population);
	return 0;
	

}