from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles


@main.route('/')
def index():
    '''
    View root page function that returns index page and the various news sources
    '''
    title = 'Home- Welcome News Highlights Website'
    # Getting the news sources
    news_sources = get_sources('sources')
    return render_template('index.html', title = title, sources = news_sources)

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    View source page function that returns a source page and its data
    '''
    title = f"{source_id} page"
    #title = "Hello"
    articles = get_articles(source_id)
    return render_template('articles.html',title = title, articles = articles)
