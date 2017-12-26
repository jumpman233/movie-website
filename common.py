import json
from media import Movie


# read a json file and return data of dict type
def open_json(file_str):
    with open(file_str) as json_file:
        data = json.load(json_file)
        return data


# transform a dict type argument to a list within Movie instances
def dict_to_movies(data):
    return [
        Movie(
            movie['title'],
            movie['story_line'],
            movie['img_url'],
            movie['trailer_url'],
            movie['type']
        ) for movie in data
    ]
