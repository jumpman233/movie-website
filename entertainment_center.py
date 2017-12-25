import fresh_tomatoes
import common

# get data
datas = common.open_json('data.json');

# transform data to movies
movies = common.dict_to_movies(datas)

# get html
fresh_tomatoes.open_movies_page(movies);
