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
double B_mn(int m, int n)
{
	return ((1 + pow((-1),(m+1)))*(1 + pow((-1),(n+1))))/pow((m*n),3);
}
double u_anal(double x, double y, double t, int M, int N)
{
	int n=0;
	int m=0;
	double t1 = 576.0/pow(M_PI,6);
	double u0 = 0.0;
	for (n=1; n<N; n++)
	{
		for (m=1; m<M; m++)
		{
			u0 += B_mn(m,n)*sin(0.5*m*M_PI*x)*sin(n*M_PI*y/3.0)*cos(M_PI*sqrt(9*pow(m,2) + 4*pow(n,2))*t);
		}
	}
	u0 = t1*u0;
	return u0;
}
int main()
{
	int i,j,t;
	
	FILE *fp;
	char nomeArquivo[100];
  
	double **u3;
	double dx = 0.01;	
	double dy = 0.00;

	u3 = alocaMatriz(N_x, N_y);
  	
  	dy = dx; 
  	double x,y;

  	

	// Initial condition.
	
	x = 0.0;
	for(i=0; i<N_x; i++)
	{ 
		y = 0.0;		
		for(j=0; j<N_y; j++)
		{
		   u3[i][j] = 0;
		  y += dy;
		}
		x += dx;
	}

	// Iteracao no tempo para a funcao analitica.
	for(i=0; i<N_x; i++)
	{ 
		for(j=0; j<N_y; j++)
		{
			u3[i][j] = u_anal(i*dx,j*dx,0.5,50,50);				
		}
	}
	sprintf(nomeArquivo,"t%03d.dat",500);
	fp = abreArquivo(nomeArquivo,"w");
	imprimeGrafico(u3, fp);
	fclose(fp);
}



















