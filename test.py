import WazeRouteCalculator
import logging
from combination import c
import time

real_time = []
for coordinates in c:
    # logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
    # logger.setLevel(logging.DEBUG)
    # handler = logging.StreamHandler()
    # logger.addHandler(handler)
    from_address, to_address = coordinates

    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address)  # , region='MA'
    real_time.append(route.calc_route_info())


