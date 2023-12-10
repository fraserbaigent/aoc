#include <iostream>
#include "../../lib/file_reader.hpp"

#include "valve.hpp"
#include <unordered_map>
#include <vector>

class Solver {
private:
    std::unordered_map<std::string, ValvePtr> _valves;
public:


    void addValve(std::string const& name,
		  int const flow_rate,
		  std::vector<std::string> const& tunnels) {
	auto it = _valves.find(name);
	if (it != _valves.end()) {
	    _valves[name] = std::make_shared<Valve>();
	}
	
	for (auto & tunnel : tunnels) {
	    auto it = _valves.find(tunnel);
	    if (it != _valves.end()) {
		_valves[tunnel] = std::make_shared<Valve>();
	    }
	    _valves[name]->addTunnel(_valves[tunnel]);
	}
    }
    

int main()
{
    auto reader = FileReader("test_data.dat");
    auto answer { 0 };
    
    std::cout << "Answer: " << answer <<"\n";
    
    return 0;
}
