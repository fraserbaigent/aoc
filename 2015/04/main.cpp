#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include "md5.hpp"

std::vector<std::string> parse_input() {
    std::ifstream infile = std::ifstream("data.dat");
    std::vector<std::string> data;
    std::string line;
    while (getline(infile, line)) {
	data.push_back(line);
    };
    return data;
};

std::string hash_string(std::string const& key, size_t const int_to_append) {
    std::string const string_to_hash = key + std::to_string(int_to_append);
    return MyMd5::do_md5(string_to_hash);
};

bool is_good_hash(std::string const& hashed_data, std::string const& comparison) {
    return hashed_data.substr(0, comparison.size()) == comparison;
};

size_t find_result(std::vector<std::string> const& data, std::string const& comparison) {
    std::stringstream ss;
    ss.imbue(std::locale(""));
    
    std::string const& key = data[0];
    
    size_t i { 0 };
    do {
	if (i % 1000 == 0) {
	    ss << std::fixed << i;
	    std::cout << ss.str() << " iterations\r" << std::flush;
	    ss.str("");
	};
	std::string const hashed_data = hash_string(key, i);
	if (is_good_hash(hashed_data, comparison)) {
	    break;
	} else {
	    i++;
	};
    } while (true);
    return i;
};
void do_part_1(std::vector<std::string> const& data) {
    size_t const result = find_result(data, "00000");
    std::cout << "\nPart 1: " << result <<"\n";
};

void do_part_2(std::vector<std::string> const& data) {
    size_t const result = find_result(data, "000000");
    std::cout << "\nPart 2: " << result <<"\n";
};

int main(int, char *[])
{
    std::vector<std::string> data = parse_input();
    do_part_1(data);
    do_part_2(data);
    return 0;
}
