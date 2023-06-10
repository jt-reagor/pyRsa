#include<iostream>
#include<random>

using namespace std;

random_device rd;
default_random_engine el(rd());

void gen_key(long long &n, long long &e, long long &d);
long long findPrime(int size);
bool fermatTest(long long p, int trials);
long long modexp(long long x, long long a, long long n);


//TODO: implement large integers (blech)


int main(){
	long long n, e, d;
	gen_key(n, e, d);
	cout << n << endl;
	return 0;
}

void gen_key(long long &n, long long &e, long long &d){
	long long p, q;
	p = findPrime(10);
	q = findPrime(10);
	cout << "Primes are " << p << " and " << q << endl;
	n = p * q;
}

long long findPrime(int size){
	while(true){
		long long prime = 1;
		for(int i=0; i<size-2; i++){
			// cout << "Prime = " << prime << endl;
			prime = prime << 1;
			if(rand()%2 == 1) prime++;
		}
		prime = (prime << 1) + 1;
		// cout << "Checking " << prime << endl;
		if(fermatTest(prime, 2)) return prime;
	}
}

bool fermatTest(long long p, int trials){
	uniform_int_distribution<long long> uni(2, p-1);
	for(int i=0; i<trials; i++){
		long long a = uni(el);
		if(modexp(a, p-1, p) != 1) return false;
	}
	return true;
}

long long modexp(long long x, long long a, long long n){
	long long z = 1;
	while(a){
		if(a % 2 == 1){
			z = z * x % n;
		}
		a = a >> 1;
		z = z * z % n; 
	}
	return z;
}