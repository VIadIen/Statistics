import datetime
from sqlalchemy.orm import Session
import statistic.models as models
import statistic.schemas as schemas


# check repeat post
def check_post(db: Session, date_post: datetime.date):
    return db.query(models.Statistic).filter(models.Statistic.date == date_post).first()


# update database post
def update_post(db: Session, post: schemas.StatisticPost):
    db_update_post = db.query(models.Statistic).filter(models.Statistic.date == post.date).first()
    db_update_post.views += post.views
    db_update_post.clicks += post.clicks
    db_update_post.cost += round(post.cost, 2)
    db.commit()
    db.refresh(db_update_post)
    return db_update_post


# add database post
def add_statistic(db: Session, post: schemas.StatisticPost):
    db_new_post = models.Statistic(date=post.date,
                                   views=post.views,
                                   clicks=post.clicks,
                                   cost=round(post.cost, 2))
    db.add(db_new_post)
    db.commit()
    db.refresh(db_new_post)
    return db_new_post


# show and order by statistics
def select_statistic(db: Session, start, end, order):
    a = {"date": models.Statistic.date, "views": models.Statistic.views, "clicks": models.Statistic.clicks,
         "cost": models.Statistic.cost}
    if order not in a.keys():
        order = "date"
    return db.query(models.Statistic).filter(start <= models.Statistic.date).filter(
        models.Statistic.date <= end).order_by(a[order]).all()
