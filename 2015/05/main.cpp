#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "string_matcher.hpp"

std::vector<std::string> parse_input() {
    std::ifstream infile = std::ifstream("data.dat");
    std::vector<std::string> data;
    std::string line;
    while (getline(infile, line)) {
	data.push_back(line);
    };
    return data;
};

int get_total_nice_strings(std::vector<std::string> const& data, bool const is_part_one) {
    int total = 0;
    StringMatcher matcher;
    for (auto const& line : data) {
	if ((is_part_one && matcher.is_nice_string(line)) || (!is_part_one && matcher.is_part_two_nice_string(line))) {
	    total +=1;
	};
    };
    return total;
};

void do_part_1(std::vector<std::string> const& data) {
    int result = get_total_nice_strings(data, true);
    
    std::cout << "Part 1: " << result <<"\n";
};

void do_part_2(std::vector<std::string> const& data) {
    int result = get_total_nice_strings(data, false);
    std::cout << "Part 2: " << result <<"\n";
};

int main(int, char *[])
{
    std::vector<std::string> data = parse_input();
    do_part_1(data);
    do_part_2(data);
    return 0;
}
