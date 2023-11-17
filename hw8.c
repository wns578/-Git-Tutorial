#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
//double pow(double a, double b); // a의 b승을 반환
//double sqrt(double x);  // 루트 x를 반환

double SD(double *n)
{
	double average, a;
	average = (n[0] + n[1] + n[2] + n[3] + n[4]) / 5;
	a = pow(n[0] - average, 2) +
		pow(n[1] - average, 2) +
		pow(n[2] - average, 2) +
		pow(n[3] - average, 2) +
		pow(n[4] - average, 2);
	a /= 5;
	return sqrt(a);
}

int main()
{
	double n[5], sd;
	printf("Enter 5 real numbers: ");
	scanf("%lf", &n[0]);
	scanf("%lf", &n[1]);
	scanf("%lf", &n[2]);
	scanf("%lf", &n[3]);
	scanf("%lf", &n[4]);
	sd=SD(n);
	printf("\nStandard Deviation = %lf", sd);
	return 0;
}