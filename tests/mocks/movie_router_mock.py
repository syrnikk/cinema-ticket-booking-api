from app.models.movie import Movie
from app.models.user import User, Role
from fastapi_pagination import Page
from app.schemas.movie_schema import MovieCreate, MovieUpdate

movie_create = MovieCreate(
    title="New Movie",
    category_id=1,
    age_restrictions=12,
    description="A new movie",
    image="movie.jpg",
    trailer_link="https://example.com",
    duration_minutes=120,
    release_date="2023-06-25"
)

movie_update = MovieUpdate(
    title="Updated Movie",
    category_id=1,
    age_restrictions=12,
    description="An updated movie",
    image="updated_movie.jpg",
    trailer_link="https://example.com/updated",
    duration_minutes=150,
    release_date="2023-06-25"
)

class MockMovieService:
    async def get_movies(self):
        return Page[Movie](items=[
            Movie(id=1, title="Movie 1"),
            Movie(id=2, title="Movie 2"),
            Movie(id=3, title="Movie 3")
        ], total=3)

    async def get_movie(self, movie_id: int):
        if movie_id == 1:
            return Movie(id=1, title="Movie 1")
        else:
            return None
    
    async def create_movie(self, movie_create: MovieCreate):
        return Movie(id=1, title=movie_create.title)
    
    async def update_movie(self, movie_id: int, movie_update: MovieUpdate):
        if movie_id == 1:
            return Movie(id=1, title="Updated Movie")
        else:
            return None
    
    async def delete_movie(self, movie_id: int):
        if movie_id == 1:
            return Movie(id=1, title="Deleted Movie")
        else:
            return None

class MockUser:
    role = Role.ADMIN