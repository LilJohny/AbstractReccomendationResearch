# Simple Flask Recommender Server

## Available requests:
- GET "/available_films"
  - Returns list of films titles, that server supports
- GET "/recommend?num=<number of films to recommend>&likes=[<sequence of film titles, user likes, separated by comma>]"
  - Example : GET "http://127.0.0.1:5000/recommend?num=4&likes=["Hellsing"]" 
### Executed and tested with Python 3.9