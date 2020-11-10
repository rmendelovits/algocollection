"""This is a demo file showing you how to use the package."""

from algocollection.common import AlgorithmClient

import pytest


def test_sandbox():
    algorithm_client = AlgorithmClient()
    print("\n")
    # YOUR CODE STARTS HERE
    primes = [2, 3, 5, 7, 11]
    print("Run linear search on primes with 7.")
    print(algorithm_client.run("LinearSearch", {'array': primes, 'key': 7}))
    print("Run binary search on primes with 7.")
    print(algorithm_client.run("BinarySearch", {'array': primes, 'key': 7}))

    print("Algorithm history:")
    print(algorithm_client.algorithm_invoker.history)
