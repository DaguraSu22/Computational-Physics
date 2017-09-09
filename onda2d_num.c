#include "stdlib.h"
#include "stdio.h"
#include "math.h"
#define M_PI 3.14159265358979323846
int N_x=200, N_y=300;
double a = 2.0, b = 3.0;

void imprimeGrafico(double **V, FILE *fp)
{
	int i,j;
	double x, y;
	double dx,dy;

	dx = 0.01;
	dy = dx;
	x = 0.0;
	for(i=0; i<N_x; i++)
	{
		y = 0.0;		
		for(j=0; j<N_y; j++)
		{
			fprintf(fp, "%7.5f %7.5lf %7.5lf\n",x, y, V[i][j]);
			y += dy;		
		}
		x += dx;
		fprintf(fp,"\n");
		
	}
}
double ** alocaMatriz(int nlinhas, int ncolunas)
{
	double **matriz;
	int i;
	// Alocacao das linhas.
	matriz = (double **) malloc(sizeof(double)*nlinhas);
	// Teste de alocacao.
	if(!matriz)
	{
		fprintf(stderr,"Erro ao alocar linhas da matriz!\n");
		exit(1);
	}
	// Alocacao das colunas.
	for(i=0; i<nlinhas;i++)
	{
		matriz[i] = (double *) malloc(sizeof(double)*ncolunas);
		// Teste de alocacao.
		if(!matriz[i])
		{
			fprintf(stderr,"Erro ao alocar colunas da matriz!\n");
			exit(1);
		}
	}
	return matriz;
}
FILE * abreArquivo(char nome[], char modo[])
{
	FILE *fp;
	fp = fopen(nome, modo);
	if(!fp)
	{
		perror(nome);
		exit(1);
	}
	return fp;
}
int main()
{
	int i,j,t; // i, j indices da grade e t o tempo.
	
	FILE *fp;
	char nomeArquivo[100];
  
	double **u0, **u1, **u2, **temp;	// n-1, n, n+1
	double dx = 0.01, dy = 0.00;	// dx = a/N_x
	double x,y,r;
	double c = 6.0; // Velocidade de propagacao da onda.
	
	dy = dx; 
  	r = 0.5;	// Numero de Courant.
	
	u0 = alocaMatriz(N_x, N_y);
	u1 = alocaMatriz(N_x, N_y);
	u2 = alocaMatriz(N_x, N_y);
	
	// Condicao inicial.	
	x = 0.0;
	for(i=0; i<N_x; i++)
	{ 
		y = 0.0;		
		for(j=0; j<N_y; j++)
		{
		  u0[i][j] = x*y*(2-x)*(3-y);
		  u1[i][j] = 0;
		  u2[i][j] = 0;
		  y += dy;
		}
		x += dx;
	}

	fp = abreArquivo("t000.dat","w");
	imprimeGrafico(u0, fp);
	fclose(fp);

	// Primeira iteracao.
	for(i=1; i<N_x-1; i++)
	{ 
		for(j=1; j<N_y-1; j++)
		{
			u1[i][j] = u0[i][j] + 0.5*r*(u0[i+1][j] + u0[i-1][j] 
			- 4.0*u0[i][j] + u0[i][j+1] + u0[i][j-1]);
		}
	}
	
	// dt = 0.001.

	// Demais iteracoes.
	for(t=1; t<=500;t++)
	{
		for(i=1; i<N_x-1; i++)
		{ 
			for(j=1; j<N_y-1; j++)
			{
				u2[i][j] = 2.0*u1[i][j] - u0[i][j] + r*(u1[i+1][j] + 
				u1[i-1][j] + u1[i][j+1] + u1[i][j-1] - 4.0*u1[i][j]);
			}
		}
		if((t%250)==0)
		{
			sprintf(nomeArquivo,"t%03d.dat",t);
			fp = abreArquivo(nomeArquivo,"w");
			imprimeGrafico(u2, fp);
			fclose(fp);
		}
		if((t%500)==0)
		{
			sprintf(nomeArquivo,"t%03d.dat",t);
			fp = abreArquivo(nomeArquivo,"w");
			imprimeGrafico(u2, fp);
			fclose(fp);
		}
		temp = u0;	
		u0 = u1;
		u1 = u2;
		u2 = temp;
	}
}
