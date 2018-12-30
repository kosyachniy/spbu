#include <opencv2\opencv.hpp>
#include "PLUQ.h"

void HouseHolderQR(const cv::Mat &A, cv::Mat &Q, cv::Mat &R)
{
    assert(A.channels() == 1);
    assert(A.rows >= A.cols);
    auto sign = [](double value) { return value >= 0 ? 1 : -1; };
    const auto totalRows = A.rows;
    const auto totalCols = A.cols;
    R = A.clone();
    Q = cv::Mat::eye(totalRows, totalRows, A.type());
    for (int col = 0; col < A.cols; ++col)
    {
        cv::Mat matAROI = cv::Mat(R, cv::Range(col, totalRows), cv::Range(col, totalCols));
        cv::Mat y = matAROI.col(0);
        auto yNorm = norm(y);
        cv::Mat e1 = cv::Mat::eye(y.rows, 1, A.type());
        cv::Mat w = y + sign(y.at<double>(0, 0)) *  yNorm * e1;
        cv::Mat v = w / norm(w);
        cv::Mat vT; cv::transpose(v, vT);
        cv::Mat I = cv::Mat::eye(matAROI.rows, matAROI.rows, A.type());
        cv::Mat I_2VVT = I - 2 * v * vT;
        cv::Mat matH = cv::Mat::eye(totalRows, totalRows, A.type());
        cv::Mat matHROI = cv::Mat(matH, cv::Range(col, totalRows), cv::Range(col, totalRows));
        I_2VVT.copyTo(matHROI);
        R = matH * R;
        Q = Q * matH;
    }
}

int main()
{
    cv::Mat A = (cv::Mat_<double>(4, 4) << 1, 1, 1, -1, 
                                           1, 1, 1, -2, 
                                           1, 1, 2,  4,
                                           1, 1, 2,  4);
    ///std::cout << A << '\n';
    
    /*cv::Mat Q = A.clone(), R = A.clone();
    HouseHolderQR(A, Q, R);
    std::cout << Q * R << '\n';*/
    PLUQ pluq(A);

    auto PLUQ = pluq.getPLUQ();
    std::cout << std::get<0>(PLUQ).t() * std::get<1>(PLUQ) * std::get<2>(PLUQ) * std::get<3>(PLUQ).t() << '\n';
    std::cout << std::get<1>(PLUQ) << '\n';
    std::cout << std::get<2>(PLUQ) << '\n';


    std::cout << "Deter:" << pluq.getDeterminant() << '\n';

    std::cout << "Rank:" << pluq.getRank() << '\n';

    std::cout << "Solve SLE: " << '\n';// << pluq.solveSLE((cv::Mat_<double>(4, 1) << 1, 1, 1, 0)) << '\n';
    std::cout << A * pluq.solveSLE((cv::Mat_<double>(4, 1) << 1, 1, 0, 0)) << '\n';

    std::cout << "Inverse: " << '\n';
    std::cout << pluq.getInverse() << '\n';
    std::cout << A * pluq.getInverse() << '\n';
    std::cout << pluq.getInverse() * A << '\n';

    std::cout << "Conditional Number: " <<pluq.getConNumb() << '\n';

    std::getchar();
    return 0;
}