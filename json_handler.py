
import json

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"movies": [], "tvseries": []}

def add_movie(data, movie):
    data['movies'].append(movie.to_dict())

def add_tvseries(data, tvseries):
    data['tvseries'].append(tvseries.to_dict())

def delete_movie(data, title):
    data['movies'] = [movie for movie in data['movies'] if movie['title'] != title]

def delete_tvseries(data, title):
    data['tvseries'] = [series for series in data['tvseries'] if series['title'] != title]
