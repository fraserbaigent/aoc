#include <iostream>
#include "../../lib/file_reader.hpp"
#include <vector>
#include <regex>
#include <set>
#include <unordered_map>

using Coordinate = std::pair<int, int>;

int manhattanDistance(Coordinate const& source,
		      Coordinate const& destination) {
    return std::abs(destination.second - source.second) +
	std::abs(destination.first - source. first);
}

class SensorArray {
private:
    Coordinate const _source;
    int const _manhattan_distance { 0 };
public:
    SensorArray(Coordinate && source,
		Coordinate const& destination)
	: _source{std::move(source)}
	, _manhattan_distance{manhattanDistance(_source, destination)}
    {
    }

    Coordinate const& getSourceCoordinate() const& {
	return _source;
    }
    
    int getX() const {
	return _source.first;
    }
    
    int getY() const {
	return _source.second;
    }
    
    void print() const {
	std::cout << "(" << _source.first <<", "<<_source.second<<") d="<<_manhattan_distance<<"\n";
    }

    int getManhattanDistance() const {
	return _manhattan_distance;
    }
};

std::vector<SensorArray> ingestSourceFile(FileReader & readfile) {
    std::vector<SensorArray> arrays;
    std::regex expression("^Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)$");
    while (readfile.good()) {
	auto line = readfile.nextLine();
	std::smatch match;
	std::regex_match(line, match, expression);
	Coordinate source{
	    std::stoi(match[1]),
	    std::stoi(match[2])};
	Coordinate const destination{
	    std::stoi(match[3]),
	    std::stoi(match[4])};
	arrays.push_back(SensorArray(std::move(source), destination));
    }
    
    return arrays;
};

using Span = Coordinate;

std::vector<Span> getSpansAtRow(std::vector<SensorArray> const& sensors, int const row_number) {
    std::vector<Span> spans;
    for (auto & sensor : sensors) {
	int y_delta = std::abs(sensor.getY() - row_number);
	int cols = std::max(sensor.getManhattanDistance() - y_delta, 0);
	if (cols >= 0) {
	    spans.push_back(Span{sensor.getX() - cols, sensor.getX() + cols});
	}
    }
    return spans;
}

void sortSpans(std::vector<Span> & spans) {
    std::sort(spans.begin(),
	      spans.end());
}

int getDistance(Span const& span) {
    return span.second - span.first;
}

int calculateCoverage(std::vector<Span> const& spans) {
    int count { 0 };
    auto span = spans[0];
    for (int i = 1; i < spans.size(); ++i) {
	auto & new_span = spans[i];
	if (new_span.first > span.second) {
	    count += getDistance(span);
	    span = new_span;
	} else if (new_span.second > span.second) {
	    span.second = new_span.second;
	}
    }
    count += getDistance(span);
    return count;
}

void solvePart1(std::vector<SensorArray> const& sensors, int const row_number) {
    std::vector<Span> spans = getSpansAtRow(sensors, row_number);
    sortSpans(spans);
    int covered_cols = calculateCoverage(spans);
    std::cout << "Answer: " << covered_cols <<"\n";
}

int getTuningFrequency(Coordinate const& coordinate) {
    return coordinate.first * 4e6 + coordinate.second;
}

std::vector<Coordinate> getCrossover(SensorArray const& left,
				     SensorArray const& right) {

    return {}
}

void solvePart2(std::vector<SensorArray> const& sensors) {
    std::unordered_map<int, std::unordered_set<int>> possibilities;
    for (int i = 0; i < sensors.size() - 1; ++i) {
	auto const& sensor_l = sensors[i];
	for (int j = 1; j < sensors.size(); ++j) {
	    auto const& sensor_r = sensors[j];
	    std::vector<Coordinate> crossovers = getCrossover(sensor_l, sensor_r);
	    for (auto & c : crossovers) {
		possibilities[c.first].emplace(c.second);
	    }
	}
    }
    for (auto & s : sensors) {
	for (auto &k : possibilities) {
	    for (auto y_it = k.second.begin(); y_it != k.second.end() && !k.second.empty();) {
		Coordinate coord{k.first, *y_it};
		if (manhattanDistance(s.getSourceCoordinate(), coord) <= s.getManhattanDistance()) {
		    k.second.erase(y_it);
		} else {
		    y_it++;
		}
	    }
	}
    }
    Coordinate answer;
    for (auto & k : possibilities) {
	if (k.second.size() == 1) {
	    answer = Coordinate{k.first, *k.second.begin()};
	    break;
	}
    }
    
    std::cout << "Answer: " << getTuningFrequency(answer) <<"\n";
}

int main()
{
    auto reader = FileReader("data.dat");
    auto sensors = ingestSourceFile(reader);

    solvePart2(sensors);
    return 0;
}
