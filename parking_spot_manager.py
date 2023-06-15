class parking_spot:
    def __init__(self, name, city, district, ptype, longitude, latitude) :
        self.__item = {'name' : name, 'city' : city, 'district' : district, 'ptype' : ptype, 'longitude' : longitude, 'latitude' : latitude}

    def get(self, keyword = 'name'):
        return self.__item[keyword]
    
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
def str_list_to_class_list(str_list):
    class_list = []
    for info in str_list:
        data = info.split(",")
        name = data[1]
        city = data[2]
        district = data[3]
        ptype = data[4]
        longitude = data[5]
        latitude = data[6]
        spot = parking_spot(name, city, district, ptype, longitude, latitude)

        class_list.append(spot)
    return class_list

def print_spots(spots):
    length = len(spots)
    print(f"---print elements({length})---")
    for spot in spots:
        print(spot)


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)