#include "stdlib.h"
#include "stdio.h"
#include "math.h"

double num, den, erro;
double **dif;

dif = alocaMatriz(N_x, N_y);

for(i=0; i<N_x; i++)
{
	for(j=0; j<N_y; j++)
	{
		num += u3[i][j] - u2[i][j];
		den += u3[i][j];
	}
}
erro = sqrt(num*num)/sqrt(den*den);
printf("%f", erro);
