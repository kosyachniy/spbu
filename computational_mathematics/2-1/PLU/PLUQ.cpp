#include "PLUQ.h"


PLUQ::PLUQ(cv::Mat originMat) : _originMat(originMat)
{
	decompose();
}

std::tuple<cv::Mat, cv::Mat, cv::Mat, cv::Mat> PLUQ::getPLUQ()
{
	return { _P.clone(),_L.clone(),_U.clone(),_Q.clone() };
}

double PLUQ::getDeterminant()
{
	determinant();
	return _determinant;
}

int PLUQ::getRank()
{
	return _rank;
}

cv::Mat PLUQ::getInverse()
{
	inverse();
	return _inverse.clone();
}

double PLUQ::getConNumb()
{
	conditionalNumber();
	return _conditionalNumber;
}

cv::Mat PLUQ::solveSLE(cv::Mat b)
{
	cv::Mat y = cv::Mat::zeros(_originMat.rows, 1, CV_64F);

	b = _P * b;
	y.at<double>(0) = b.at<double>(0);

	for (int i = 1; i < _originMat.rows; ++i)
	{
		double sum = 0.0;
		for (int j = 0; j < i; ++j)
		{
			sum += y.at<double>(j) * _L.at<double>(i, j);
		}
		y.at<double>(i) = b.at<double>(i) - sum;
	}


	for (int i = 0; i < _U.rows; ++i) 
	{
		if (cv::countNonZero(_U.row(i)) == 0 && y.at<double>(i) != 0)
		{

			std::cout << "Error!" << '\n';
			system("pause");
			exit(-1);
		}
	}
	cv::Mat x = cv::Mat::zeros(_originMat.rows, 1, CV_64F);
	if (_U.at<double>(_originMat.rows - 1, _originMat.cols - 1) != 0)
	{
		x.at<double>(_originMat.rows - 1, 0) = y.at<double>(_originMat.rows - 1) / _U.at<double>(_originMat.rows - 1, _originMat.cols - 1);
	}
	else
	{
		x.at<double>(_originMat.rows - 1, 0) = y.at<double>(_originMat.rows - 1);
	}
	for (int i = 2; i < _originMat.rows + 1; ++i)
	{
		double sum = 0.0;
		for (int j = 1; j < i; ++j)
		{
			sum += x.at<double>(_originMat.rows - j, 0) * _U.at<double>(_originMat.rows - i, _originMat.cols - j);
		}
		if (_U.at<double>(_originMat.rows - i, _originMat.rows - i) != 0)
		{
			x.at<double>(_originMat.rows - i, 0) = (y.at<double>(_originMat.rows - i) - sum) / _U.at<double>(_originMat.rows - i, _originMat.rows - i);
		}
		else
		{
			x.at<double>(_originMat.rows - i, 0) = (y.at<double>(_originMat.rows - i) - sum);
		}
	}
	return _Q * x;
}

void PLUQ::conditionalNumber()
{
	_conditionalNumber = cv::norm(_inverse) * cv::norm(_originMat);
}

void PLUQ::inverse()
{
	cv::Mat inv = cv::Mat::zeros(_originMat.rows, _originMat.cols, CV_64F);
	for (int i = 0; i < _originMat.rows; ++i)
	{
		cv::Mat z = cv::Mat::zeros(_originMat.rows, 1, CV_64F);
		z.at<double>(i, 0) = 1;
		cv::Mat s = solveSLE(z);
		for (int j = 0; j < _originMat.rows; ++j) 
		{
			inv.at<double>(j, i) = s.at<double>(j);
		}
	}
	_inverse = inv.clone();
}

void PLUQ::matSwap(cv::Mat A, cv::Mat B)
{
	cv::Mat tmp(A.clone());
	B.copyTo(A);
	tmp.copyTo(B);
}

void PLUQ::decompose()
{
	cv::Mat C(_originMat.clone());

	cv::Mat P(cv::Mat::eye(C.rows, C.cols, CV_64F));
	cv::Mat Q(cv::Mat::eye(C.rows, C.cols, CV_64F));

	int rank = C.rows;
	int maxElRow = -1;
	int maxElCol = -1;

	for (int i = 0; i < C.rows; ++i) {

		double pivotValue = 0;
		for (int row = i; row < C.rows; ++row)
		{
			for (int col = i; col < C.cols; ++col)
			{
				if (fabs(C.at<double>(row, col)) > pivotValue) {
					pivotValue = fabs(C.at<double>(row, col));
					maxElRow = row;
					maxElCol = col;
				}
			}
		}
		if (pivotValue < 10e-16)
		{
			rank -= 1;
			continue;
		}

		matSwap(C.row(i), C.row(maxElRow));
		matSwap(C.col(i), C.col(maxElCol));

		matSwap(P.row(i), P.row(maxElRow));
		matSwap(Q.col(i), Q.col(maxElCol));

		for (int row = i + 1; row < C.rows; ++row)
		{
			C.at<double>(row, i) /= C.at<double>(i, i);
			for (int col = i + 1; col < C.cols; ++col)
			{
				C.at<double>(row, col) -= C.at<double>(row, i) * C.at<double>(i, col);
			}
		}
	}
	cv::Mat lower = cv::Mat::eye(C.rows, C.cols, CV_64F);
	cv::Mat	upper = cv::Mat::zeros(C.rows, C.cols, CV_64F);

	for (int row = 0; row < C.rows; ++row)
	{
		for (int col = 0; col < C.cols; ++col)
		{
			if (row > col)
			{
				lower.at<double>(row, col) = C.at<double>(row, col);
			}
			else
			{
				upper.at<double>(row, col) = C.at<double>(row, col);
			}
		}
	}
	_P = P.clone();
	_L = lower.clone();
	_U = upper.clone();
	_Q = Q.clone();
	_rank = rank;
}

void PLUQ::determinant()
{
	double det = 1.0;
	for (int i = 0; i < _U.rows; ++i)
	{
		det *= _U.at<double>(i, i);
	}
	if (_U.rows % 2 == 1 && _U.rows != 1)
	{
		det *= -1;
	}
	_determinant = det;
}
