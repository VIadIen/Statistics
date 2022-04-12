# Statistics

This microservice was designed to calculate statistics.

You have three at your functions: adding, deleting and displaying statistics data.


Below is the function for adding a record.
<pre>
|     |     |     |     |     |     |     |
⌄     ⌄     ⌄     ⌄     ⌄     ⌄     ⌄     ⌄

@app.post("/static/add", response_model=schemas.StatisticPost)
def post_new_stat(post: schemas.StatisticPost, db: Session = Depends(get_db)):
    db_new_post = crud.check_post(db, date_post=post.date)
    if db_new_post:
        return crud.update_post(db=db, post=post)
    return crud.add_statistic(db=db, post=post)</pre>
    
    
This  function receives input data ("date", "views", "clicks", "cost"), which will later be entered into the database. 


The next function for get statistics.
<pre>
|     |     |     |     |     |     |     |
⌄     ⌄     ⌄     ⌄     ⌄     ⌄     ⌄     ⌄

@app.get("/static/show")
async def get_statistic(order: str, start_date: datetime.date, end_date: datetime.date, db: Session = Depends(get_db)):
    query = crud.select_statistic(db=db, start=start_date, end=end_date, order=order)
    return query</pre>
    
You enter the start date of the period, the end date and the field by which the sorting will be performed (by default "date").

Then the function returns sorted statistics with new fields: "cpc" - average cost per click and "cpm" - average cost of 1000 views.
The "cpc" and "cpm" fields are not available for sorting, because they are not saved anywhere.

The last function is cleare database function.
<pre>
|     |     |     |     |     |     |     |
⌄     ⌄     ⌄     ⌄     ⌄     ⌄     ⌄     ⌄

@app.delete("/static/clear")
def delete_statistic(db: Session = Depends(get_db)):
    res = db.query(models.Statistic).delete()
    db.commit()
    return {"status": f"Delete {res} posts"}</pre>
    
It's very simple function, it uses the capabilities of SQLAlchemy to delete all posts in the database    

**If you need more information, you can download my repository and view other components.**
