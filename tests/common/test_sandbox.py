"""This is a demo file showing you how to use the package."""

from algocollection.common import AlgorithmClient

import pytest


def test_sandbox():
    algorithm_client = AlgorithmClient()
    print("\n")
    # YOUR CODE STARTS HERE
    primes = [73, 13, 43, 47, 83, 97, 71, 79, 17, 19, 3, 37,
              41, 61, 67, 5, 23, 7, 89, 11, 29, 31, 2, 59, 53]
    print("Run linear search on primes with 7.")
    print(algorithm_client.run("linear_search", {'array': primes, 'key': 7}))
    sorted_primes = algorithm_client.run("selection_sort", {'array': primes})
    print("Run binary search on primes with 7.")
    print(algorithm_client.run("binary_search",
                               {'array': sorted_primes, 'key': 7}))

    print("Algorithm history:")
    print(algorithm_client.algorithm_invoker.history)
