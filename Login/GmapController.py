import googlemaps

# needed libs:
# 	pip install -U googlemaps
# how to use google map:
# 1. create object
# 	gmap = Gmap()
# 2. location info to lat & lan
# 	lo = gmap.geo_encode('123 West 106th Street 3A, New York, NY')
# 	lat = (lo[0]['geometry']['bounds']['northeast']['lat'] + lo[0]['geometry']['bounds']['southwest']['lat'])/2
# 	lng = (lo[0]['geometry']['bounds']['northeast']['lng'] + lo[0]['geometry']['bounds']['southwest']['lng'])/2
# 3. lat & lan to location info
# 	lo_info = gmap.geo_decode(lat,lng)
# 4. url to google map:
# 	https://www.google.com/maps/search/?api=1&query='lat','lng'
# 	or
# 	https://www.google.com/maps/search/?api=1&query=123+West+106th+Street+New+York+NY


class Gmap:
    KEY = 'AIzaSyBRdolJRdcoL0uOWK0MBwSmMyNnvovU_Xg'

    def __init__(self):
        self.gmaps = googlemaps.Client(key=self.KEY)

    def geo_encode(self, lo_word):
        encode_res = self.gmaps.geocode(lo_word)
        return encode_res

    def geo_decode(self, lat, lng):
        decode_res = self.gmaps.reverse_geocode((lat, lng))
        return decode_res


def get_state(address):
    gmap = Gmap()
    succeed = False
    try:
        state = gmap.geo_encode(address)
        components = state[0]['address_components']
        for component in components:
            if component['types'][0] == 'administrative_area_level_1':
                state = component['long_name']
        succeed = True
        return state
    finally:
        if not succeed:
            return 'FAILURE'


def get_coordinate(address):
    gmap = Gmap()
    succeed = False
    try:
        lo = gmap.geo_encode(address)
        lat = lo[0]['geometry']['location']['lat']
        lng = lo[0]['geometry']['location']['lng']
        succeed = True
        return str([lat, lng])
    finally:
        if not succeed:
            return 'FAILURE'
