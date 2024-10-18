def calculate_area(length, breadth):
    area_sqft = length * breadth
    area_sqyd = area_sqft / 9  # Convert sqft to sqyd
    return area_sqft, area_sqyd
