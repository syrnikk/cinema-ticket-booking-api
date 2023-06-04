from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from app.routers import auth_router, movie_router, category_router, cinema_router, repertoire_router, screening_router, \
    user_router, reservation_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router.router)
app.include_router(movie_router.router)
app.include_router(category_router.router)
app.include_router(cinema_router.router)
app.include_router(repertoire_router.router)
app.include_router(screening_router.router)
app.include_router(user_router.router)
app.include_router(reservation_router.router)

# Add pagination
add_pagination(app)
