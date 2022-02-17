import WazeRouteCalc
import pandas as pd
import logging
from combination import combs
import time
from datetime import datetime
import sys

zones={}
zones['real_time']=[]
zones['static']=[]

t=0
for c in combs:
    print(c)
    sys.exit(0)
    real_time = []
    for coordinates in c:
        logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        logger.addHandler(handler)
        from_address, to_address = coordinates

        route = WazeRouteCalc.WazeRouteCalculator(from_address, to_address, region='MA')#
        r=route.calc_route_info()
        real_time.append(r)
        time.sleep(0.5)
    zones['real_time'].append(real_time)
    static = []
    for coordinates in c:
        logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        logger.addHandler(handler)
        from_address, to_address = coordinates
        route = WazeRouteCalc.WazeRouteCalculator(from_address, to_address, region='MA') #
        static.append(route.calc_route_info(real_time=False))
        time.sleep(0.5)
    zones['static'].append(static)
    t=t+1
    print(f'zone: {t}')

result=pd.DataFrame.from_dict(zones)

curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
result.to_csv(curr_datetime+'.csv')