#include <iostream>
#include "../../lib/file_reader.hpp"
#include <vector>
#include <cmath>

class Solver {
private:
    std::vector<int> _b5_vals = std::vector<int>(10, 0);
public:
    Solver() {
	
	for (int i = 0; i < 10; ++i) {
	    _b5_vals[i] = std::pow(5,i);
	}
    }
    
    int snafuToBaseTen(std::string const& value) {

    }

    std::string baseTenToSnafu(int const value) {
	
    }
}

int main()
{
    auto reader = FileReader("data.dat");
    auto answer { 0 };
    
    std::cout << "Answer: " << business <<"\n";
    
    return 0;
}
