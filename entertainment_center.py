import fresh_tomatoes
import common

datas = common.open_json('data.json');

movies = common.dict_to_movies(datas)

fresh_tomatoes.open_movies_page(movies);
