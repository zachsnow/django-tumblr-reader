import os

from django.conf import settings

# Tumblr blog to embed in your site; change this to your own blog!
# This is the default blog embedded by {% tumblr_posts %}.
BLOG = getattr(settings, 'TUMBLR_READER_BLOG', 'djangotumblrreader')

# The default number of posts that will be embedded by {% tumblr_posts %}.
COUNT = getattr(settings, 'TUMBLR_READER_COUNT', 10)

# Posts with this tag will be embedded by {% tumblr_posts %}.
# by default.
TAGGED = getattr(settings, 'TUMBLR_READER_TAGGED', '')

# The default callback to use when embedding posts using {% tumblr_posts %}.
CALLBACK = getattr(settings, 'TUMBLR_READER_CALLBACK', 'tumblrReaderCallback')

# The default container into which posts embedded using {% tumblr_posts %}
# should be written; the default is the empty string, which means that
# posts will be written into the same container as the template tag.
CONTAINER = getattr(settings, 'TUMBLR_READER_CONTAINER', '') 

# The url at which Tumblr Reader static files will be served. 
MEDIA_URL = getattr(settings, 'TUMBLR_READER_MEDIA_URL', os.path.join(settings.MEDIA_URL, '/tumblr/')
                    
# The directory from which Tumblr Reader static files will be served when
# using the development server; for production you should ensure that this
# directory is served at `settings.TUMBLR_READER_MEDA_URL` by your static file
# web server! 
MEDIA_ROOT = getattr(settings, 'TUMBLR_READER_MEDIA_ROOT', os.path.join(settings.MEDIA_ROOT, '/tumblr/'))
