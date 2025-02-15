def lon_converter_to_idx(longitude):
    new_lon=(180.625+longitude)/0.625
    return int(new_lon)
def lat_converter_to_idx(latitude):
    new_lat=(181+2*latitude)
    return int(new_lat)