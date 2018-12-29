#include "mpi.h"
#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
    int id, numprocs, buffer = 15, start, size, tag = 0;
    char mes[buffer];

    strcpy(mes, "rabotay please");

    MPI_Status status;
    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &start);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    double time_start = MPI_Wtime();
    int end = (start + 1) % size;
    MPI_Send(mes, buffer, MPI_CHAR, end, tag, MPI_COMM_WORLD);
    end = (size + start - 1) % size;

    MPI_Recv(&mes, buffer, MPI_CHAR, end, tag, MPI_COMM_WORLD, &status);
    double time_end = MPI_Wtime();

    double delta = time_end - time_start;
    cout << "Process №" << start << " (time: " << delta << ")" << endl; 

    if (start != size - 1) {
        int end = (start + 1) % size;
        MPI_Send(mes, buffer, MPI_CHAR, end, tag, MPI_COMM_WORLD);
    }

    MPI_Finalize();

    return 0;
}