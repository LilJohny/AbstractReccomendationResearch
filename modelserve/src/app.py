from flask import Flask
from flask import request

from constants import MOVIE_TO_NETFLIX_ID_DICT, AVAILABLE_MOVIES_TITLES
from model import get_recommendations

app = Flask(__name__)


@app.route('/available_films')
def available_films():
    return {"available_films": list(AVAILABLE_MOVIES_TITLES)}


def invalid(film_name):
    return film_name not in AVAILABLE_MOVIES_TITLES


@app.route('/recommend')
def recommend_view():
    num_of_films_to_recommend = request.args.get("num")
    likes = request.args.get("likes").strip("[]").split(",")
    likes = list(map(lambda x: x.replace('"', '').strip(), likes))

    if any(map(lambda x: not x.isnumeric(), list(num_of_films_to_recommend))):
        return {"error": "Number of recommendations is not a number."}
    elif num_of_films_to_recommend is None:
        return {"error": "Provide number of films to recommend."}
    elif likes is None:
        return {"error": "Provide names of films, that user already likes."}
    else:
        bad_films = list(filter(invalid, likes))
        if len(bad_films) != 0:
            return {"error": f"This version of app don`t knows about some films you passed.",
                    "unknown_films": bad_films}
        else:
            likes_ids = list(map(lambda x: MOVIE_TO_NETFLIX_ID_DICT[x], likes))
            num_of_films_to_recommend = int(num_of_films_to_recommend)
            recommendation = get_recommendations(likes_ids, num_of_films_to_recommend)
            return {"status": "ok", "recommendations": recommendation}


if __name__ == '__main__':
    app.run()
