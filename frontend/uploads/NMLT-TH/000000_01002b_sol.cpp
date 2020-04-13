#include <fstream>
#include <string>
#include <time.h>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <sstream>

using namespace std;

void printDetail(double length, int option, double result)
{
	cout << setprecision(10) << fixed;
	cout << "option " << option << ": Length" << length << " => Result:" << result << "\n";
}

double ConvertLength(double length, int option)
{
	switch (option)
	{
	case 1:
		return length * pow(10, -3);
	case 2:
		return length * pow(10, 3);
	case 3:
		return length * 393700787;
	case 4:
		return length / 393700787;
	default:
		throw "Invalid input";
	}
}

int main(int narg, char **argv)
{
	ifstream ifs;
	ifs.open(argv[1]);
	int option;
	double length;
	int count = 0;
	string line;
	try
	{
		while (ifs >> line)
		{
			if(count == 0)
			{
				stringstream ss(line);
				ss >> length;
				count++;
			}
			else
			{
				stringstream ss(line);
				ss >> option;
			}
		}
		double result = ConvertLength(length, option);
		printDetail(length, option, result);
	}
	catch (char const *s)
	{
		printf("An exception occurred. Exception type: %s\n", s);
	}

	ifs.close();
	return 0;
}

