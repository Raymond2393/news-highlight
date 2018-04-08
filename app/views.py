from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home- Welcome to News Highlight Website'
    # Getting the news source

    news_sources = get_sources('sources')
    return render_template('index.html',title = title, sources = news_sources)

@app.route('/articles/<source_id>')
def articles(source_id):
    '''
    View source page function that returns a source page and its data
    '''
    title = f"{source_id} page"
    #title = "Hello"
    articles = get_articles(source_id)
    return render_template('articles.html',title = title, articles = articles)
