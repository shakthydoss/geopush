
def write_to_es(es, index, doc_type, body,id=None):
    rec = es.index(index, doc_type=doc_type, body=body,id=id)
    return rec

def search_by_lat_lon(es,lat,lon,distance):
    query = {
            "query": {
                "filtered": {
                    "query": {
                        "match_all": {}
                    },
                    "filter": {
                        "geo_distance": {
                            "distance": "1km",
                            "location": {
                                "lat": 13.153412,
                                "lon": 79.897104
                                 }
                            }
                        }
                    }
                }
            }
    res = es.search(index="ping", doc_type='chennai', body=query)
    return res

