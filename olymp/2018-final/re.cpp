#include <iostream>
#include <fstream>
#include <locale>
#include <iomanip>
#include <sstream>
#include <string>
 
struct SpaceOut : std::numpunct<wchar_t>
{
 wchar_t do_decimal_point() const
 {
  return L'';
 }
 wchar_t do_thousands_sep() const
 {
  return L'';
 }
 std::string do_grouping() const
 {
  return "\3";
 }
};
 
std::wstring ToWString(double x)
{
 std::wstringstream Stream;
 std::wstring       Result;
 Stream.imbue(std::locale(Stream.getloc(), new SpaceOut));
 Stream<<std::setprecision(11);
 Stream<<std::fixed;
 Stream<<x;
 Result=Stream.str();
 return Result;
}
int main()
{
 std::wcout<<ToWString(1234567890e+20)<<std::endl;
 return 0;
}