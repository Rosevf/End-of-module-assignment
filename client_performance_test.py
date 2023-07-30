import timeit
import cProfile
from client import Client

def test_client_performance():
    # Creating an instance of the Client class
    client = Client()
    
    # Measuring the execution time of the connect_server method
    execution_time = timeit.timeit(client.connect_server, number=1)
    
    # Printing the execution time
    print("Client Execution Time:", execution_time, "seconds")

def test_client_profiling():
    # Creating an instance of the Client class
    client = Client()
    
    # Setting up a profiler to measure function performance
    profiler = cProfile.Profile()
    
    # Running the profiler on the connect_server method
    profiler.runctx("client.connect_server()", globals(), locals())
    
    # Printing the profiling statistics
    profiler.print_stats()

if __name__ == "__main__":
    # Running the performance test for the client
    test_client_performance()
    
    # Running the profiling test for the client
    test_client_profiling()