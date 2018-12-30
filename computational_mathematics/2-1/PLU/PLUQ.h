#pragma once
#include <opencv2\opencv.hpp>


class PLUQ
{
public:
    PLUQ(cv::Mat originMat);

    std::tuple<cv::Mat, cv::Mat, cv::Mat, cv::Mat> getPLUQ();
    double getDeterminant();
    int getRank();
    cv::Mat getInverse();
    double getConNumb();

    cv::Mat solveSLE(cv::Mat b);
private:
    cv::Mat _originMat;
    cv::Mat _P;
    cv::Mat _L;
    cv::Mat _U;
    cv::Mat _Q;
    int _rank;
    double _determinant;
    cv::Mat _inverse;
    double _conditionalNumber;

    void conditionalNumber();
    void inverse();
    void matSwap(cv::Mat A, cv::Mat B);
    void decompose();
    void determinant();
};

