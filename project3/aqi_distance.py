
def range_aqi(pm: float) -> int:
    '''
    uses the linear interpolation function to convert pm to aqi then find the range given the list of tuples
    '''
    pm_list = [(0, 12.0), (12.1, 35.4), (35.5, 55.4), (55.5, 150.4), (150.5, 250.4), (250.5, 350.4), (350.5, 500.4)]
    aqi_list = [(0, 50), (51, 100), (101, 150), (151, 200), (201, 300), (301, 400), (401, 500)]

    for i in range(len(pm_list)):
        if type(pm) in (float, int) and pm >= pm_list[i][0] and pm <= pm_list[i][1]:
            aqi = _linear_interpolation(pm, pm[i][0], pm_list[i][1], aqi_list[i][0], aqi_list[i][1])
            return aqi
        elif pm == None:
            return 0


#private function

def _linear_interpolation(pm: float, min_pm: float, max_pm: float, min_aqi: float, max_aqi: float) -> int:
    '''
    calculates the linear interpolation between PM to AQI and returns the conversion
    '''
    # y = y1 + ((x – x1) / (x2 – x1)) * (y2 – y1) + 0.5(round up)
    standard = int(min_aqi + 0.5 + ((pm - min_pm) / (max_pm - min_pm)) * (max_aqi - min_aqi))
    return standard




