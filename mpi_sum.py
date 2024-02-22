# Run in terminal something like: mpirun -n 5 python mpi_sum.py
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(f'This process is rank {rank}')

# initialise sum of ranks array
rankSum = np.zeros(1)
rank = np.array(float(rank))

# communication happens, then node 0 receives the sum of ranks (rankSum)
comm.Reduce(rank,rankSum,op=MPI.SUM,root=0)

# root process prints results
if comm.rank == 0:
	print(f'The sum of ranks is {rankSum[0]}')