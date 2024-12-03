#include "string_matcher.hpp"
#include <iostream>
#include <string>
#include <unordered_map>

void test_matcher() {
    std::cout << "Testing Part 1\n";
    StringMatcher const matcher;

    std::unordered_map<std::string, bool> const tests {
	{"ugknbfddgicrmopn", true},
	{"aaa", true},
	{"jchzalrnumimnmhp", false},
	{"haegwjzuvuyypxyu", false},
	{"dvszwmarrgswjxmb", false},
    };

    for (auto const& test : tests) {
	bool const result = matcher.is_nice_string(test.first);
	if (result != test.second) {
	    std::cout << "FAILED - " << test.first << " is " << (result == true ? "nice" : "naughty")
		      <<" (expected " << (test.second == true ? "nice" : "naught y") <<")\n";
	} else {
	    std::cout << "PASSED - " << test.first << " is " << (test.second == true ? "nice" : "naughty") <<"\n";
	};
    };
};

void test_matcher_part_2() {
    std::cout << "Testing Part 2\n";
    StringMatcher const matcher;


    std::unordered_map<std::string, bool> const tests {
	{"qjhvhtzxzqqjkmpb", true},
	{"xxyxx", true},
	{"uurcxstgmygtbstg", false},
	{"ieodomkazucvgmuy", false},
    };


    for (auto const& test : tests) {
	bool const result = matcher.is_part_two_nice_string(test.first);
	if (result != test.second) {
	    std::cout << "FAILED - " << test.first << " is " << (result == true ? "nice" : "naughty")
		      <<" (expected " << (test.second == true ? "nice" : "naughty") <<")\n";
	} else {
	    std::cout << "PASSED - " << test.first << " is " << (test.second == true ? "nice" : "naughty") <<"\n";
	};
    };    
};

int main(int , char *[])
{
    test_matcher();
    test_matcher_part_2();
    
    return 0;
}
