import secrets
from typing import Any, List, Dict

from flask import Flask, Response, request, jsonify

app = Flask(__name__)

movies: List[Dict[str, Any]] = [
    {"id": 1, "title": "The Godfather", "year": 1972, "genre": "Crime", "poster": "https://br.web.img3.acsta.net/medias/nmedia/18/90/93/20/20120876.jpg"},
    {"id": 2, "title": "The Shawshank Redemption", "year": 1994, "genre": "Drama","poster": "https://upload.wikimedia.org/wikipedia/pt/d/d2/The_Shawshank_Redemption_p%C3%B4ster.png"},
    {"id": 3, "title": "Schindler's List", "year": 1993, "genre": "Biography","poster": "https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
    {"id": 4, "title": "Raging Bull", "year": 1980, "genre": "Biography", "poster": "https://upload.wikimedia.org/wikipedia/pt/f/fe/Raging_Bull_%281980%29_Film_Poster.jpg"},
    {"id": 5, "title": "Casablanca", "year": 1942, "genre": "Romance", "poster": "https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg"},
    {"id": 6, "title": "Citizen Kane", "year": 1941, "genre": "Drama", "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Citizen_Kane_poster%2C_1941_%28Style_B%2C_unrestored%29.jpg/800px-Citizen_Kane_poster%2C_1941_%28Style_B%2C_unrestored%29.jpg"},
]

@app.route("/auth", methods=["POST"])
def auth() -> Response:
    """
    Perform authentication
    """
    data: Any = request.get_json()
    if (
        {"username", "password"}.issubset(data)
        and data["username"] == "bob"
        and data["password"] == "bob"
    ):
        access_token: str = secrets.token_urlsafe()
        refresh_token: str = secrets.token_urlsafe()
        print(access_token)
        return jsonify(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "status": "success",
            }
        )
    return jsonify({"status": "login failed"}), 401


@app.route("/movies", methods=["GET"])
def get_movies() -> Response:
    """
    Get all movies
    """
    return jsonify(movies)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=19003)
