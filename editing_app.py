import datetime
import functools
import os
import re
import urllib

from flask import (Flask, flash, Markup, redirect, render_template, request,
                   Response, session, url_for)
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base


# Blog configuration values.

# You may consider using a one-way hash to generate the password, and then
# use the hash again in the login view to perform the comparison. This is just
# for simplicity.
ADMIN_PASSWORD = 'secret'
APP_DIR = os.path.dirname(os.path.realpath(__file__))

# The playhouse.flask_utils.FlaskDB object accepts database URL configuration.
engine = create_engine('sqlite:///%s' % os.path.join(APP_DIR, 'blog.db'), echo=True)

DEBUG = False


# The secret key is used internally by Flask to encrypt session data stored
# in cookies. Make this unique for your app.
SECRET_KEY = """MIIEpAIBAAKCAQEA4fcY79HoEFKrBwpFQsc+Ivl538ycbC6ujGvIWrfZSlBE6oK5hrTRHeHa/med1NDu87zVku9byR6+/1jZUzJgVFT5avzysl07DLL9yqjOGioyluot6sLyrqCErqc5UmNRfynlmTQEJUwE64BGbig8i2FrY1hTfgHQWklc3pN7NvQInjcO6Za5/hZG6YRam2UmWkWZvnWMDAdq5q8Ze6BIoX1M9vVkSyPqj4ZSr65CP/9na7Rc/ZmSc3pDtrLEAT45Gnoka7H4XKs6MHQvIAq44fEDSVlrFC0rAdg4s4ZjBJ/ZbwlunNSJU4CCuMKBBgQ/bKgOyO6Y61rQoH/JTm7fKwIDAQABAoIBACZVcweMRqAuRhFlrqZLgsEQLZrH7Wl06eushUrOkbBHuclG8A5oMmmtXSd3kJD/+OmkiV7p+FpAOwq6mfPBQhJMcBu0Wb/kjRX0b5Wn2X8a1YZAqBWBiQYS+S9f8xuE+dhm1SqOZn2lTdhd5JTfgpXqqvspitB/okcO1xBzWJ3Tqt4Bs2Hb9RCcmVeMq8CRYAC5fc95+Qso5n764E0fKkHlCjHUR6rgqOz95Vh299C5C9Ua60qHU7MACnf4B8dn39wBF6KPzxCP/9Npb2KGTALYXzqbsy+YC/byhscoPpTcNikX2NuNS2q2ilPFVtiNPDviJJ4MJ7O4LuwoarDwKoECgYEA85dY54KJKqpcyF6Bn6mTSDeIhnKEhPXEx6v+zMULe8d0RJh6FXvW+npeSvCF8EUvnrNsrra2g6oOVuPuYZbyXVepoOq4kf/weyEo/fp2BGXSuh/SFIEsFXtf1JSCWn4Z0RovZRfhuP/5LYhV/cvAiGhT7gonTIBbbLYlqMmpZuECgYEA7XnkJ5jNweDhSKjOP2f2PDdtZOCliZIYDEZ+ByzyHV8MTN+lIlftekqC1gC6QDYDlEOFs/Q12l9qyTmuPU+MZLiF6yxvwrud9In95jjWdENIMN7bnfhhknChbeQvPE7UQB2ixs37io7j04BI5pAmCij6Ffb9Upd8Z7rXmQELY4sCgYEA1jSuQo+AzZsYkj7BIEU/tg7XqNtFe6KgE7JFE47nZUblEHlBSmkniAZZqu7N6Zb9pEJF/XHBGBFQIMq5UuopYTn4egBOpFz7/VsQsB8y7vUXlQLse4mH2bAvekHKS4d+bmnnaa/RmBzI42hzrgYh3hJYVAhrvJNXUkbu4PnNVSECgYBDtaNl3t2b0ACr9OWJkpzUooEgaCUKyorsxRSd+yS1VypsqL+uwR9G5QPU/LQeJshyd6YhnxnTv6z03utdM9c1yJ72ZN8gyNnKpaWtBLuwvpZQyNoZen5ngJGmgY8uRNOjzE9jG8wCv6cZ4NPoWWVfNDvKE3g7GlIwSUe7ql6S7QKBgQDlmfAWbDaAVI9mkXp2MGXFm8/yGNiOinVuDQfkXEy74qPyRHzMvc5ACZuuRSaS9kE97EvWAMNRgSKQRZS1plms8QpYyHLBRMdSipd429bF3oZXmL6tC/VCXO+7yLGKEtQv46aXUfdxRd2PZLBb2+3afsw/Q6bLGCVMVSm+xL4wxw=="""

# This is used by micawber, which will attempt to generate rich media
# embedded objects with maxwidth=800.
SITE_WIDTH = 800


# Create a Flask WSGI app and configure it using values from the module.
app = Flask(__name__)
app.config.from_object(__name__)

# FlaskDB is a wrapper for a peewee database that sets up pre/post-request
# hooks for managing database connections.
#flask_db = FlaskDB(app)
Base = declarative_base()

# The `database` is the actual peewee database, as opposed to flask_db which is
# the wrapper.
#database = flask_db.database



# Configure micawber with the default OEmbed providers (YouTube, Flickr, etc).
# We'll use a simple in-memory cache so that multiple requests for the same
# video don't require multiple network requests.
oembed_providers = bootstrap_basic(OEmbedCache())

class Entry(Base):
    __tablename__ = 'Entry'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    slug = Column(String, unique=True)
    content = Text()
    published = Boolean(index=True)
    # maybe create artificial dates on posts
    timestamp = DateTime(default=datetime.datetime.now, index=True)

    def __repr__(self):
        return "<User(title={0}, slug={1}, content={2}, published={3})>".format(self.name, self.)

    @property
    def html_content(self):
        """
        Generate HTML representation of the markdown-formatted blog entry,
        and also convert any media URLs into rich media objects such as video
        players or images.
        """
        hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
        extras = ExtraExtension()
        markdown_content = markdown(self.content, extensions=[hilite, extras])
        oembed_content = parse_html(
            markdown_content,
            oembed_providers,
            urlize_all=True,
            maxwidth=app.config['SITE_WIDTH'])
        return Markup(oembed_content)

    def save(self, *args, **kwargs):
        # Generate a URL-friendly representation of the entry's title.
        if not self.slug:
            self.slug = re.sub('[^\w]+', '-', self.title.lower()).strip('-')
        # just commit the database?
        ret = super(Entry, self).save(*args, **kwargs)

        # Store search content.
        #self.update_search_index()
        return ret

    # # create a new row...
    # def update_search_index(self):
    #     # Create a row in the FTSEntry table with the post content. This will
    #     # allow us to use SQLite's awesome full-text search extension to
    #     # search our entries.
    #     query = (FTSEntry
    #              .select(FTSEntry.docid, FTSEntry.entry_id)
    #              .where(FTSEntry.entry_id == self.id))
    #     try:
    #         fts_entry = query.get()
    #     except FTSEntry.DoesNotExist:
    #         fts_entry = FTSEntry(entry_id=self.id)
    #         force_insert = True
    #     else:
    #         force_insert = False
    #     fts_entry.content = '\n'.join((self.title, self.content))
    #     fts_entry.save(force_insert=force_insert)

    @classmethod
    def public(cls):
        return Entry.select().where(Entry.published == True)

    @classmethod
    def drafts(cls):
        return Entry.select().where(Entry.published == False)

    # @classmethod
    # def search(cls, query):
    #     words = [word.strip() for word in query.split() if word.strip()]
    #     if not words:
    #         # Return an empty query.
    #         return Entry.select().where(Entry.id == 0)
    #     else:
    #         search = ' '.join(words)

    #     # Query the full-text search index for entries matching the given
    #     # search query, then join the actual Entry data on the matching
    #     # search result.
    #     return (FTSEntry
    #             .select(
    #                 FTSEntry,
    #                 Entry,
    #                 FTSEntry.rank().alias('score'))
    #             .join(Entry, on=(FTSEntry.entry_id == Entry.id).alias('entry'))
    #             .where(
    #                 (Entry.published == True) &
    #                 (FTSEntry.match(search)))
    #             .order_by(SQL('score').desc()))

class FTSEntry(Base):
    entry_id = Integer()
    content = Text()

    # class Meta:
    #     database = base

def login_required(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        if session.get('logged_in'):
            return fn(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return inner

@app.route('/login/', methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next') or request.form.get('next')
    if request.method == 'POST' and request.form.get('password'):
        password = request.form.get('password')
        # TODO: If using a one-way hash, you would also hash the user-submitted
        # password and do the comparison on the hashed versions.
        if password == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            session.permanent = True  # Use cookie to store session.
            flash('You are now logged in.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            flash('Incorrect password.', 'danger')
    return render_template('login.html', next_url=next_url)

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        return redirect(url_for('login'))
    return render_template('logout.html')

@app.route('/')
def index():
    search_query = request.args.get('q')
    if search_query:
        query = Entry.search(search_query)
    else:
        query = Entry.public().order_by(Entry.timestamp.desc())

    # The `object_list` helper will take a base query and then handle
    # paginating the results if there are more than 20. For more info see
    # the docs:
    # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#object_list
    return object_list(
        'index.html',
        query,
        search=search_query,
        check_bounds=False)

def _create_or_edit(entry, template):
    if request.method == 'POST':
        entry.title = request.form.get('title') or ''
        entry.content = request.form.get('content') or ''
        entry.published = request.form.get('published') or False
        if not (entry.title and entry.content):
            flash('Title and Content are required.', 'danger')
        else:
            # just need to save here
            entry.save()
            flash('Entry saved successfully.', 'success')
            if entry.published:
                return redirect(url_for('detail', slug=entry.slug))
            else:
                return redirect(url_for('edit', slug=entry.slug))

    return render_template(template, entry=entry)

@app.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    return _create_or_edit(Entry(title='', content=''), 'create.html')

@app.route('/drafts/')
@login_required
def drafts():
    query = Entry.drafts().order_by(Entry.timestamp.desc())
    return object_list('index.html', query, check_bounds=False)

@app.route('/<slug>/')
def detail(slug):
    if session.get('logged_in'):
        query = Entry.select()
    else:
        query = Entry.public()
    # TODO: what does `get_object_or_404` do?
    entry = get_object_or_404(query, Entry.slug == slug)
    return render_template('detail.html', entry=entry)

@app.route('/<slug>/edit/', methods=['GET', 'POST'])
@login_required
def edit(slug):
    # TODO: what does `get_object_or_404` do?
    entry = get_object_or_404(Entry, Entry.slug == slug)
    return _create_or_edit(entry, 'edit.html')

@app.template_filter('clean_querystring')
def clean_querystring(request_args, *keys_to_remove, **new_values):
    # We'll use this template filter in the pagination include. This filter
    # will take the current URL and allow us to preserve the arguments in the
    # querystring while replacing any that we need to overwrite. For instance
    # if your URL is /?q=search+query&page=2 and we want to preserve the search
    # term but make a link to page 3, this filter will allow us to do that.
    querystring = dict((key, value) for key, value in request_args.items())
    for key in keys_to_remove:
        querystring.pop(key, None)
    querystring.update(new_values)
    return urllib.urlencode(querystring)

@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Not found</h3>'), 404

def main():
    database.create_tables([Entry, FTSEntry], safe=True)
    app.run(debug=True)

if __name__ == '__main__':
    main()