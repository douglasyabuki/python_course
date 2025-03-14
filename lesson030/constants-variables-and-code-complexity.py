"""
CONSTANT = "Variables" that will not change
Many conditions in the same if (bad practice)
    <- Complexity count (bad practice)
"""
speed = 61  # current speed of the car
car_location = 100  # location of the car on the road

RADAR_1 = 60  # maximum speed of radar 1
LOCATION_1 = 100  # location of radar 1
RADAR_RANGE = 1  # The distance range where the radar detects

car_speed_exceeds_radar_1 = speed > RADAR_1
car_passed_radar_1 = car_location >= (LOCATION_1 - RADAR_RANGE) and \
    car_location <= (LOCATION_1 + RADAR_RANGE)
car_fined_radar_1 = car_passed_radar_1 and car_speed_exceeds_radar_1

if car_speed_exceeds_radar_1:
    print('Car speed exceeded radar 1 limit')

if car_passed_radar_1:
    print('Car passed radar 1')

if car_fined_radar_1:
    print('Car was fined by radar 1')
