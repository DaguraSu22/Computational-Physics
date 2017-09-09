double B_mn(int m, int n)
{
	return ((1 + (-1)^(m+1))*(1 + (-1)^(n+1)))/(m*n)^3
}
double u_anal(double x, double y, double t, int M, int N)
{
	int n=0;
	int m=0;
	double t1 = 576.0/M_PI^6;
	double u0 = 0.0;
	for (n=1; n<N; n++)
	{
		for (m=1; m<M; m++)
		{
			u0 += B_mn(m,n)*sin(0.5*m*M_PI*x)*sin(n*M_PI*y/3.0)*cos(M_PI*sqrt(9*m^2 + 4*n^2)*t);
		}
	}
	u0 = t1*u0;
	return u0;

}