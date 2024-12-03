#ifndef STRING_MATCHER
#define STRING_MATCHER
#include <algorithm>
#include <unordered_set>
#include <string>
#include <unordered_map>
#include <vector>

#include <iostream>

class StringMatcher {
private:
    std::unordered_set<std::string> const forbidden_strings { "ab", "cd", "pq", "xy" };
    std::unordered_set<char> const vowels {'a','e','i','o','u'};
public:
    bool is_nice_string(std::string const& line) const {
	bool double_letter { false };
	int seen_vowels = 0;
	for( size_t i { 0 }; i < line.size(); ++i) {
	    if (i > 0) {
		std::string const& trial = line.substr(i - 1, 2);
		if (forbidden_strings.find(trial) != forbidden_strings.cend()) {
		    return false;
		};
		if (!double_letter && line[i] == line[i-1]) {
		    double_letter = true;
		};
	    };
	    if (vowels.find(line[i])!=vowels.cend()) {
		seen_vowels+=1;
	    };
	    
	};
	return seen_vowels >= 3 && double_letter == true;
    };

    bool is_part_two_nice_string(std::string const& line) const {
	bool has_repeat_between {false};
	bool has_repeat_pair {false};

	std::unordered_map<std::string, std::vector<int>> seen_pairs;
	
	for (size_t i { 0 } ; i < line.size(); ++i) {
	    if (i < line.size() - 2) {
		if (line[i] == line[i+2] && line[i] != line[i+1]) {
		    has_repeat_between = true;
		};
	    };
	    if (i > 0) {
		std::string const& trial = line.substr(i - 1, 2);
		std::vector<int> &seen = seen_pairs[trial];
		bool const is_repeat = std::find(seen.cbegin(), seen.cend(), i-1) != seen.cend();
		if (seen.size() >= (is_repeat ? 2 : 1)) {
		    has_repeat_pair = true;
		};
		seen.push_back(i);
	    };
	};
	
	return has_repeat_between && has_repeat_pair;
    };
};

#endif
