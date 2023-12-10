#ifndef VALVE_HPP
#define VALVE_HPP

#include <unordered_set>
#include <memory>

using ValvePtr = std::shared_ptr<class Valve>;

class Valve {
private:
    std::unordered_set<ValvePtr> _tunnel_locations;
    int _flow_rate { 0 };
public:
    void addTunnel(ValvePtr const& valve) {
	_tunnel_locations.insert(valve);
    }

    void setFlowRate(int const flow_rate) {
	_flow_rate = flow_rate;
    }

    int flowRate() const {
	return _flow_rate;
    }
};

#endif
