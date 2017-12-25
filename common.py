import json
import media

def open_json(file_str):
	with open(file_str) as json_file:
		data = json.load(json_file)
		return data

def dict_to_movies(data): 
	movies = [];
	for i in data:
		movies = [media.Movie(i['title'], i['story_line'], i['img_url'], i['trailer_url'], i['type'])] + movies;		
	return movies;