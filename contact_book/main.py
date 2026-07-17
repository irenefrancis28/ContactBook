from fastapi import FastAPI


from contact_book.routers.contacts import router as contact_router
from contact_book.routers.groups import router as group_router
from contact_book.database import engine
import contact_book.database_models as database_models
from contact_book.database import init_db
from contact_book.database import group_init_db

app = FastAPI()

app.include_router(contact_router)
app.include_router(group_router)

database_models.Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup():
   init_db()
   group_init_db()




