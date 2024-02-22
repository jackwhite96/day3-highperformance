# Run in terminal something like: mpirun -n 5 python mpi_ranks.py
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(f'This process is rank {rank}')