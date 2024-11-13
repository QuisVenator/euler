package main

import (
	"fmt"
	"math"
)

const (
	MAX_N = 24001
	MAX_K = 12001
)

var (
	div_k           [MAX_N][]int // Array of slices to store divisors
	min_k           [MAX_K]int   // Stores minimal N for each k
	k_not_found     = MAX_K - 2  // Since k starts from 2
	lowest_unfound_k = 2         // Tracks the lowest k not yet found
)

// Function to calculate divisors for numbers up to MAX_N
func calculateDivisors() {
	for n := 2; n < MAX_N; n++ {
		divisors := make([]int, 0)
		for i := 2; i <= n/2; i++ {
			if n%i == 0 {
				divisors = append(divisors, i)
			}
		}
		divisors = append(divisors, n) // Include n itself
		div_k[n] = divisors
	}
	fmt.Println("Divisors calculated")
}

// Recursive function to find minimal product-sum numbers
func integerPartition(n, remaining_prod, remaining_sum, k, last_divisor int) {
	if k > MAX_K-1 {
		return
	}

	if k+remaining_sum < lowest_unfound_k {
		return
	}

	if remaining_prod == 1 {
		true_k := k + remaining_sum
		if true_k < MAX_K && min_k[true_k] == 0 {
			min_k[true_k] = n
			k_not_found--
			for i := lowest_unfound_k; i < MAX_K; i++ {
				if min_k[i] == 0 {
					lowest_unfound_k = i
					break
				}
			}
			if k_not_found == 0 {
				return
			}
		}
	}

	if remaining_sum < remaining_prod {
		return
	}

	divisors := div_k[remaining_prod]
	for _, i := range divisors {
		if i > last_divisor {
			break
		}
		integerPartition(n, remaining_prod/i, remaining_sum-i, k+1, i)
		if k_not_found == 0 {
			return
		}
	}
}

func main() {
	calculateDivisors()

	// Initialize min_k array
	for i := 0; i < MAX_K; i++ {
		min_k[i] = 0
	}

	test_num := 4
	for k_not_found > 0 {
		integerPartition(test_num, test_num, test_num, 0, math.MaxInt32)
		test_num++
		if test_num%100 == 0 {
			fmt.Printf("Progress: %d\n", k_not_found)
			fmt.Printf("Current N: %d\n", test_num)
		}
	}

	sum := 0
	found := make(map[int]bool)
	for i := 2; i < MAX_K; i++ {
		if !found[min_k[i]] {
			sum += min_k[i]
			found[min_k[i]] = true
		}
	}

	fmt.Printf("Sum of minimal product-sum numbers: %d\n", sum)
}
