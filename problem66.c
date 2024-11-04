#include <stdio.h>
#include <gmp.h>
#include <stdbool.h>

// For multithreading:#include <pthread.h> 
#include <pthread.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 

unsigned long long max_d = 0;
unsigned long long max_x = 0;
unsigned long long x = 1;
int multipliers[1001];
int total_multipliers = 0;

// Used to lock access to x, max_x and max_d
pthread_mutex_t x_lock;
pthread_mutex_t multipliers_lock;

void* calc(void *args) {
    mpz_t n;
    mpz_init(n);
    mpz_t square;
    mpz_init(square);


    while (true)
    {
        pthread_mutex_lock(&x_lock);
        mpz_set_ui(square, x);
        mpz_mul_ui(square, square, x);
        x++;
        pthread_mutex_unlock(&x_lock);

        for (int i = 2; i <= 1000; i++) {
            if (multipliers[i] == 0) {
                continue;
            }

            mpz_mul_ui(n, square, multipliers[i]);
            mpz_add_ui(n, n, 1);

            if (mpz_perfect_square_p(n)) {
                pthread_mutex_lock(&multipliers_lock);
                multipliers[i] = 0;
                total_multipliers--;
                printf("Found a square for %d, remaining multiplieres: %d\n", i, total_multipliers);
                gmp_printf("x: %Zd\n", square);
                if (x > max_x) {
                    max_x = x;
                    max_d = i;
                }
                pthread_mutex_unlock(&multipliers_lock);
            }
        }

    }
    return NULL;
}

int main() {
    pthread_mutex_init(&x_lock, NULL);
    pthread_mutex_init(&multipliers_lock, NULL);

    mpz_t n;
    mpz_init(n);
    printf("Initialized n and square\n");
    for (int i = 2; i <= 1000; i++) {
        mpz_set_ui(n, i);
        if (mpz_perfect_square_p(n)) {
            multipliers[i] = 0;
            continue;
        }

        total_multipliers++;
        multipliers[i] = i+2;
    }
    printf("Initialized multipliers\n");

    // Create the threads
    int thread_count = 16;
    pthread_t threads[thread_count];
    for (int i = 0; i < thread_count; i++) {
        pthread_create(&threads[i], NULL, &calc, NULL);
    }

    // Wait for the threads to finish
    for (int i = 0; i < thread_count; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_lock(&x_lock);
    printf("hello\n");
    pthread_mutex_unlock(&x_lock);

    printf("Max x: %llu\n", max_x);
    printf("Max d: %llu\n", max_d);
}