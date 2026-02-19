from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

text_post = {
    1 : {"title":"developing" , "content" : "we are learning pyhtnon fast api learing"}
}


@app.get("/post")
def get_post():
    return text_post

class Post(BaseModel) : 
    title : str
    content : str 

@app.post("/post")
def create_post(post: Post) :
    post_id = len(text_post)+1 
    text_post[post_id] = post 
    return text_post[post_id]
