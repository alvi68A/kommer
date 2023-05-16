import xml.etree.ElementTree as ET
import math


def getKeyInformation(filepath):
        
    tree = ET.parse(filepath)
    root = tree.getroot()

    print(len(root))
    print(len(root[1]))
    print(len(root[1][1]))

    datapoints=len(root[1][1])

    startlat = float(root[1][1][0].attrib['lat'])
    startlon = float(root[1][1][0].attrib['lon'])

    endlat = float(root[1][1][datapoints-1].attrib['lat'])
    endlon = float(root[1][1][datapoints-1].attrib['lon'])

    lat1 = math.radians(startlat)
    lat2 = math.radians(endlat)
    long1 = math.radians(startlon)
    long2 = math.radians(endlon)
    dlat= math.radians(endlat-startlat)
    dlon= math.radians(endlon-startlon)

    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    d = 6371000 * c

    
    b = math.atan2(math.sin(long2 - long1) * math.cos(lat2), math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(long2 - long1))
    b = math.degrees(b)
    b = (b + 360) % 360

    result = [datapoints, d, b, startlat, startlon]
    return(result)



