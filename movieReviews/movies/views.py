from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Movies,Ratings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import numpy as np
import pandas as pd
import pymysql
from django.contrib.auth.decorators import login_required
from . import contentbased as cb

def recommendation(request):
    connection = pymysql.connect("localhost","root","","moviereviews" )


    movies = pd.read_sql_query("SELECT * from movies_movies",connection)
    ratings = pd.read_sql_query("SELECT * from movies_ratings",connection)

    genres = []
    for a in movies.genres:
        try:
            genres.extend(a.split('|'))
        except AttributeError:
            pass

    genres = set(genres)
        
    create_date = lambda val: val[-5:-1] if val[-1] == ')' else np.nan

    movie_ratings = ratings.groupby('movieId_id')['rating']
    avg_ratings = movie_ratings.mean()
    num_ratings = movie_ratings.count()
    last_rating = ratings.groupby('movieId_id').max()['timestamp']
    
    rating_count_df = pd.DataFrame({'avg_rating': avg_ratings, 'num_ratings': num_ratings})
    rating_count_df = rating_count_df.join(last_rating)
    
   
    movie_recs = movies.set_index('id').join(rating_count_df)
   
    ranked_movies = movie_recs.sort_values(['avg_rating', 'num_ratings', 'timestamp'], ascending=False)
    
    
    ranked_movies = ranked_movies[ranked_movies['num_ratings'] > 4]


    context = {
        "object_list": ranked_movies[:12],
        "title": "List"}
    
    return render(request, "recommendation.html", context)


def post_list(request):
    userId = request.user.id
    userName = request.user.username
    queryset_list = Ratings.objects.select_related('movieId')
    
    paginator = Paginator(queryset_list, 12)  
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        
        queryset = paginator.page(1)
    except EmptyPage:
        
        queryset = paginator.page(paginator.num_pages)
    
    context = {
        "user_id":userId,
        "user_name":userName,
        "object_list": queryset,
        "title": "List"}
    return render(request, "home.html", context)

def detail(request,id):
    connection = pymysql.connect("localhost", "root", "", "moviereviews")
    ds = pd.read_sql_query("SELECT * from movies_movies", connection)

    detail = Movies.objects.get(id=id)
    results = cb.getFrames(ds)
    content = cb.recommend(item_id=id, num=5,results=results)

    context = {
        "detail":detail,
        "content":content,
    }
    return render(request, "detail.html", context)

