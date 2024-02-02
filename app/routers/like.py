import models, schemas, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter(
    prefix="/likes",
    tags=['Likes']
)

@router.post("/{post_id}")
async def like_a_post(post_id: int ,db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There is no post with id: {post_id}")

    like_query = db.query(models.Like).filter(models.Like.post_id == post_id, models.Like.user_id == current_user.id)
    liked = like_query.first()
    
    if not liked:
        new_like = models.Like(post_id = post_id, user_id = current_user.id)
        db.add(new_like)
        db.commit()
        content = {"message": "you just like the post"}
        return JSONResponse(content=content, status_code=status.HTTP_201_CREATED)
    else:
        db.delete(liked)
        db.commit()
        content = {"message": "you just dislike the post"}
        return JSONResponse(content=content, status_code=status.HTTP_204_NO_CONTENT)
        