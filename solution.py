import WazeRouteCalc
import logging
from combination import combs
import time

try:
        from_loc = f"{from_lat},{from_long}"
        to_loc   = f"{to_lat},{to_long}"

        retry_cnt = 0
        while retry_cnt < 3:
            try:
                self.count_waze_locates[devicename] += 1
                waze_call_start_time = time.time()
                route = WazeRouteCalculator.WazeRouteCalculator(
                        from_loc, to_loc, self.waze_region)

                route_time, route_distance = \
                    route.calc_route_info(self.waze_realtime)

                self.time_waze_calls[devicename] += (time.time() - waze_call_start_time)

                route_time     = round(route_time, 0)
                route_distance = round(route_distance, 2)

                return (WAZE_USED, route_distance, route_time)

            except WazeRouteCalculator.WRCError as err:
                retry_cnt += 1
                log_msg = (f"Waze Server Error (#{retry_cnt}), Retrying, Type-{err}")
                self._log_info_msg(log_msg)

    except Exception as err:
        self._set_waze_not_available_error(err)