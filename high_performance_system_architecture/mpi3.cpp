#include "mpi.h"
#include <iostream>

using namespace std;

void circle_baton(int argc, char *argv[]) {
    int id, numprocs, buffer = 11, start, size, tag = 0;
    char message[buffer];

    strcpy(message, "rabotaaaay");

    MPI_Status status;
    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &start);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    while (true) {
        double time_start = MPI_Wtime();

        int end = (start + 1) % size;
        MPI_Send(message, buffer, MPI_CHAR, end, tag, MPI_COMM_WORLD);
        end = (size + start - 1) % size;

        MPI_Recv(&message, buffer, MPI_CHAR, end, tag, MPI_COMM_WORLD, &status);

        double delta = MPI_Wtime() - time_start;
        cout << "Process №" << start << " (time: " << delta << ")" << endl; 
    }

    MPI_Finalize();
}

void circle_shift(int argc, char *argv[]) {
    int id, numprocs, buffer = 11, start, size, tag = 0;
    char send_message[buffer], rec_message[buffer];

    strcpy(send_message, "rabotaaaay");

    MPI_Status send_status, rec_status;
    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &start);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    while (true) {
        double time_start = MPI_Wtime();

        int end = (start + 1) % size;
        MPI_Request send_req;
        MPI_Isend(send_message, buffer, MPI_CHAR, end, tag, MPI_COMM_WORLD, &send_req);
        int source = (size + start - 1) % size;

        MPI_Request rec_req; 
        MPI_Irecv(&rec_message, buffer, MPI_CHAR, source, tag, MPI_COMM_WORLD, &rec_req);
        MPI_Wait(&send_req, &send_status);
        MPI_Wait(&rec_req, &rec_status);

        double delta = MPI_Wtime() - time_start;
        cout << "Process №" << start << " (time: " << delta << ")" << endl; 
    }

    MPI_Finalize();
}

void master_slave(int argc, char *argv[]) {
    int id, numprocs, buffer = 11, start, size, tag = 0;
    char message[buffer];

    strcpy(message, "rabotaaaay");

    MPI_Status status;
    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &start);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    while (true) {
        if (start == 0) {
            while (true) {
                MPI_Recv(&message, buffer, MPI_CHAR, MPI_ANY_SOURCE, tag, MPI_COMM_WORLD, &status);
                int end = status.MPI_SOURCE;

                cout << "Process №" << start  << " (from " << end << ": \"" << message << "\")" << endl; 

                MPI_Send(message, buffer, MPI_CHAR, end, tag, MPI_COMM_WORLD);
            }
        } else {
            int end = 0;

            MPI_Send(message, buffer, MPI_CHAR, end, tag, MPI_COMM_WORLD);
            MPI_Recv(&message, buffer, MPI_CHAR, end, tag, MPI_COMM_WORLD, &status);

            cout << "Process №" << start  << " (from " << end << ": \"" << message << "\")" << endl; 

        }
    }

    MPI_Finalize();
}

void every_with_every(int argc, char *argv[]) {
    int id, numprocs, buffer = 11, start, size, tag = 0;
    char message[buffer];

    strcpy(message, "rabotaaaay");

    MPI_Status status;
    MPI_Init(&argc,&argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &start);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    while (true) {
        for (int i = 0; i < size; i++) {
            if (i != start) {
                MPI_Send(message, buffer, MPI_CHAR, i, tag, MPI_COMM_WORLD);
            }
        }

        for (int i = 0; i < size; i++) {
            if (i != start) {
                MPI_Recv(&message, buffer, MPI_CHAR, i, tag, MPI_COMM_WORLD, &status);

                cout << "Process №" << start  << " (from " << i << ": \"" << message << "\")" << endl; 
            }
        }
    }

    MPI_Finalize();
}

int main (int argc, char *argv[]) {
    circle_baton(argc, argv);
    // circle_shift(argc, argv);
    // master_slave(argc, argv);
    // every_with_every(argc, argv);

    return 0;
}