import json
import media

# read a json file and return data of dict type
def open_json(file_str):
	with open(file_str) as json_file:
		data = json.load(json_file)
		return data

# transform a dict type argument to a list within Movie instances
def dict_to_movies(data): 
	movies = [];
	for i in data:
		movies = [media.Movie(i['title'], i['story_line'], i['img_url'], i['trailer_url'], i['type'])] + movies;		
	return movies;