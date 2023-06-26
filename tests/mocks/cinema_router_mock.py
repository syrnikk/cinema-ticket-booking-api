from fastapi_pagination import Page, Params
from app.models.cinema import Cinema
from app.models.user import Role


class MockCinemaService:
    async def get_cinemas(self):
            cinemas = [
                Cinema(id=1, name="Cinema 1"),
                Cinema(id=2, name="Cinema 2"),
                Cinema(id=3, name="Cinema 3"),
            ]
            total = len(cinemas)
            params = Params(page=1, size=10)
            return Page.create(items=cinemas, params=params, total=total)
    
    async def get_cinema(self, cinema_id):
        if cinema_id == 1:
            return Cinema(id=1, name="Cinema 1")
        elif cinema_id == 2:
            return Cinema(id=2, name="Cinema 2")
        else:
            return None
        
    async def create_cinema(self, cinema_create):
        return Cinema(id=1, name=cinema_create.name, location=cinema_create.location)
    
    async def update_cinema(self, cinema_id, cinema_update):
        if cinema_id == 1:
            return Cinema(id=1, name=cinema_update.name, location=cinema_update.location)
        return None
    
    async def delete_cinema(self, cinema_id):
        if cinema_id == 1:
            return Cinema(id=1, name="Deleted Cinema", location="Deleted Location")
        return None

class MockUser:
    role = Role.ADMIN