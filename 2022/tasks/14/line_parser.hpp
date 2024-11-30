#ifndef LINE_PARSER_HPP
#define LINE_PARSER_HPP

#include <vector>
#include <string>
#include <bits/stdc++.h>

using Coordinate = std::pair<int,int>;
using Line = std::pair<Coordinate, Coordinate>;
class LineParser {
private:
    static constexpr int MAX_Y { 500 };
    int _min_x { INT_MAX };
    int _max_x { 0 };
    int _max_y { 0 };
    private:
    Coordinate pairFromString(std::string const& string) {
	Coordinate coordinate {0, 0};
	auto comma = string.find(',');
	coordinate.first = std::stoi(string.substr(0, comma));
	coordinate.second = std::stoi(string.substr(comma + 1, string.size() - (comma + 1)));
	_min_x = std::min(_min_x, coordinate.first);
	_max_x = std::max(_max_x, coordinate.first);
	_max_y = std::max(_max_y, coordinate.second);
	return coordinate;
    }
    
public:
    std::vector<Line> parseInputLine(std::string const& input_line) {
	std::vector<Line> lines;
	auto left { 0 };
	auto right { 1 };
	Coordinate last_point { -1, -1 };
	do {
	    right = input_line.find(" -> ", left);
	    if (right == std::string::npos) {
		right = input_line.size();
	    }
	    auto coord = pairFromString(input_line.substr(left,right - left));
	    if (last_point.first >= 0 && last_point.second >= 0) {
		lines.push_back({last_point, coord});
	    }
	    left = right + 4;
	    last_point = coord;
	} while (right < input_line.size());
	std::cout << "Parsed " << input_line << "\n";
	return lines;
    }

    Line getGridCorners() const {
	return Line{{_min_x, 0}, {_max_x, _max_y}};
    };
	
};

#endif
