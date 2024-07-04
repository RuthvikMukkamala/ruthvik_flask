from flask import Flask, render_template, url_for, request
from flask_flatpages import FlatPages

app = Flask(__name__)

DIR_BLOG_POSTS = 'blogs'
flatpages = FlatPages(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/personal')
def personal_info():
    return render_template("personal.html")

@app.route('/research')
def research_info():
    return render_template("research.html")

@app.route('/projects')
def project_info():
    return render_template("projects.html")

# Inspired by Danie Nell
@app.route("/essays/")
def essays_info():
    posts = [p for p in flatpages if p.path.startswith(DIR_BLOG_POSTS)]

    filtered_posts = []
    for post in posts:
        published_status = getattr(post, "meta").get('published')
        if published_status == True:
            filtered_posts.append(post)

    latest = sorted(filtered_posts, reverse=True, key=lambda p: getattr(p, "meta").get('date'))

    return render_template('essays.html', posts=latest)

@app.route('/post/<name>/')
def essay(name):
    path = '{}/{}'.format(DIR_BLOG_POSTS, name)
    post = flatpages.get_or_404(path)
    return render_template('essay-post.html', post=post)




