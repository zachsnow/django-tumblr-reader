import os

from django.conf import settings

# Tumblr blog to embed in your site; change this to your own blog!
# This is the default blog embedded by {% tumblr_posts %}.
BLOG = getattr(settings, 'TUMBLR_READER_BLOG', 'django-tumblr-reader')

# The default number of posts that will be embedded by {% tumblr_posts %}.
COUNT = getattr(settings, 'TUMBLR_READER_COUNT', 10)

# Posts with this tag will be embedded by {% tumblr_posts %}.
# by default.
TAGGED = getattr(settings, 'TUMBLR_READER_TAGGED', '')

# The default container into which posts embedded using {% tumblr_posts %}
# should be written; the default is the empty string, which means that
# posts will be written into the same container as the template tag.
CONTAINER = getattr(settings, 'TUMBLR_READER_CONTAINER', '') 
