from common.algorithm_client import AlgorithmClient

# Execute if this file is run as a script and not imported as a module
if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11]

    algorithm_client = AlgorithmClient()
    print("Run linear search on primes with 2.")
    print(algorithm_client.run("LinearSearch", {'array': primes, 'key': 2}))
    print("Run linear search on primes with 7.")
    print(algorithm_client.run("LinearSearch", {'array': primes, 'key': 7}))
    print("Run linear search on primes with 6.")
    print(algorithm_client.run("LinearSearch", {'array': primes, 'key': 6}))

    print("Run binary search on primes with 2.")
    print(algorithm_client.run("BinarySearch", {'array': primes, 'key': 2}))
    print("Run binary search on primes with 7.")
    print(algorithm_client.run("BinarySearch", {'array': primes, 'key': 7}))
    print("Run binary search on primes with 6.")
    print(algorithm_client.run("BinarySearch", {'array': primes, 'key': 6}))

    # print("Algorithm history:")
    # print(algorithm_client.algorithm_invoker.history)
