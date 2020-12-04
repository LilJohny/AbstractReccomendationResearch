from src.constants import WORD_VECTORS, NETFLIX_ID_TO_MOVIE_DICT


def get_recommendations(users_likes, n=5):
    # users_likes - list of netflix film ids as string
    # topn - num most likely
    # print(WORD_VECTORS.vocab.keys())
    WORD_VECTORS.most_similar_cosmul(positive=users_likes)
    all_recommendations = []
    for like in users_likes:
        all_recommendations += WORD_VECTORS.similar_by_word(like, topn=n)

    all_recommendations = list(filter(lambda x: x[0] not in users_likes, list(set(list(all_recommendations)))))
    all_recommendations.sort(key=lambda x: x[1], reverse=True)
    all_recommendations_new = []
    used_ids = []
    for rec in all_recommendations:
        if rec[0] not in used_ids:
            all_recommendations_new.append(rec)
            used_ids.append(rec[0])
    result = []
    for recom in all_recommendations_new[:n]:
        result.append({"netflix_id": recom[0], "similarity": recom[1], "film_name": NETFLIX_ID_TO_MOVIE_DICT[recom[0]]})
    return result
