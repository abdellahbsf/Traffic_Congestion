import WazeRouteCalc
import pandas as pd
import logging
from combination import Mat
import time
from datetime import datetime

result = pd.DataFrame()
zones = []
t = 0
for z in range(22):
    zones.append([])
    c = Mat[z]
    for i in range(5):
        real_time = []
        for j in range(5):
            logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
            logger.setLevel(logging.DEBUG)
            handler = logging.StreamHandler()
            logger.addHandler(handler)
            from_address, to_address = c[i], c[j]
            route = WazeRouteCalc.WazeRouteCalculator(from_address, to_address, region='MA')
            r = route.calc_route_info()
            real_time.append(r)
            time.sleep(0.5)
        zones[z].append(real_time)

    result = result.append([zones[z]], ignore_index=True)
    t = t + 1
    print(f'zone: {t}')

curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
result.to_csv(curr_datetime+'.csv')