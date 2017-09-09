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
	// Alocação das linhas.
	matriz = (double **) malloc(sizeof(double)*nlinhas);
	// Teste de alocação.
	if(!matriz)
	{
		fprintf(stderr,"Erro ao alocar linhas da matriz!\n");
		exit(1);
	}
	// Alocação das colunas.
	for(i=0; i<nlinhas;i++)
	{
		matriz[i] = (double *) malloc(sizeof(double)*ncolunas);
		// Teste de alocação.
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
  
	// i,j indices para o grid da membrana
	// t tempo
  
	double **u0; 		// Anterior (n-1)
	double **u1; 		// Atual    (n)
	double **u2;		// Próxima  (n+1)
	double **temp;
	double **u3;
	double dx = 0.01;	
	double dy = 0.00;

	u0 = alocaMatriz(N_x, N_y);
	u1 = alocaMatriz(N_x, N_y);
	u2 = alocaMatriz(N_x, N_y);
	u3 = alocaMatriz(N_x, N_y);
  	
  	dy = dx; 
  	double c = 6.0;	// Velocidade de propagação da onda.
  	double x,y,r;

  	r = 0.5;	// Courant number.

	// Initial condition.
	
	x = 0.0;
	for(i=0; i<N_x; i++)
	{ 
		y = 0.0;		
		for(j=0; j<N_y; j++)
		{
		  u0[i][j] = x*y*(2-x)*(3-y);
		  u1[i][j] = 0;
		  u2[i][j] = 0;
		  u3[i][j] = 0;
		  y += dy;
		  //printf("%f %f \n", x, y);
		}
		x += dx;
	}

	//fp = abreArquivo("t000.dat","w");
	//imprimeGrafico(u0, fp);
	//fclose(fp);

	// para o primeiro avanco no tempo
	for(i=1; i<N_x-1; i++)
	{ 
		for(j=1; j<N_y-1; j++)
		{
			u1[i][j] = u0[i][j] + 0.5*r*(u0[i+1][j] + u0[i-1][j] - 4.0*u0[i][j] + u0[i][j+1] + u0[i][j-1]);
		}
	}
	
	//dt = 0.001;

	// itera no tempo
	for(t=1; t<=500;t++)
	{
		for(i=1; i<N_x-1; i++)
		{ 
			for(j=1; j<N_y-1; j++)
			{
				u2[i][j] = 2.0*u1[i][j] - u0[i][j] + r*(u1[i+1][j] + u1[i-1][j] + u1[i][j+1] + u1[i][j-1] - 4.0*u1[i][j]);
			}
		}

		/*if((t%250)==0)
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
		}*/
		// troca as posicoes
		// veja que usando ponteiros ha um ganho
		// pois de outra forma teriamos que ter loops
		// aninhados aqui para fazer essa troca
		temp = u0;	// temp é um variável auxiliar para a troca dos ponteiros.
		u0 = u1;
		u1 = u2;
		u2 = temp;
	}
	// Iteração no tempo para a função analítica.
	for(i=0; i<N_x; i++)
	{ 
		for(j=0; j<N_y; j++)
		{
			u3[i][j] = u_anal(i*dx,j*dx,0.5,50,50);				
		}
	}
	//sprintf(nomeArquivo,"t%03d.dat",500);
	//fp = abreArquivo(nomeArquivo,"w");
	//imprimeGrafico(u3, fp);
	//fclose(fp);
		
	
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
	sprintf(nomeArquivo,"t%03d.dat",500);
	fp = abreArquivo(nomeArquivo,"w");
	imprimeGrafico(dif, fp);
	fclose(fp);

}



















