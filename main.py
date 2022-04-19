import datetime
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import statistic.crud as crud
import statistic.schemas as schemas
import statistic.models as models
from statistic.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        yield db


# add new statistics post
@app.post("static/post", response_model=schemas.StatisticPost)
def post_new_stat(post: schemas.StatisticPost, db: Session = Depends(get_db)):
    db_new_post = crud.check_post(db, date_post=post.date)
    if db_new_post:
        return crud.update_post(db=db, post=post)
    return crud.add_statistic(db=db, post=post)


# show statistics
@app.get("static/get")
async def get_statistic(order: str, start_date: datetime.date, end_date: datetime.date, db: Session = Depends(get_db)):
    query = crud.select_statistic(db=db, start=start_date, end=end_date, order=order)
    return query


# delete post from database
@app.delete("static/delete")
def delete_statistic(db: Session = Depends(get_db)):
    res = db.query(models.Statistic).delete()
    db.commit()
    return {"status": f"Delete {res} posts"}
