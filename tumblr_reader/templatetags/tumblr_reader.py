import json

from django.conf import settings as django_settings
from django import template
from django.template import TemplateSyntaxError

from .. import settings

register = template.Library()

@register.simple_tag
def tumblr_posts(
    blog=settings.BLOG,
    count=settings.COUNT,
    tagged=settings.TAGGED,
    container=settings.CONTAINER):
    """
    Embed posts from your Tumblr blog.
    
    Syntax::
    
        {% tumblr_posts %}
        {% tumblr_posts blog="blog" %}
        {% tumblr_posts count=10 %}
        {% tumblr_posts tagged="tag 1, tag 2" %}
        {% tumblr_posts container="id" %}
    
    You can use any combination of these arguments, but you should use each
    not more than once.
    
    ``from``:
        Defaults to ``settings.TUMBLR_READER_BLOG``.
        
    ``count``:
        Defaults to ``settings.TUMBLR_READER_COUNT``.
        
    ``tagged``:
        Defaults to ``settings.TUMBLR_READER_TAGGED``.

    ``container``:
        Defaults to ``settings.TUMBLR_READER_CONTAINER``.

        You shouldn't need to specify this unless you are embedding a blog
        or blogs multiple times on a single page; in that case you almost
        certainly want to use different container ids for each embed::
            
            {% tumblr_posts container="someId" %}
            {% tumblr_posts container="anotherId" %}
        
    """
    # Not strictly necessary, just here to catch errors earlier.
    try:
        count = int(count)
    except ValueError:
        raise TemplateSyntaxError('tumblr_posts: count must be an integer')
    
    script = '<script type="text/javascript">$(function(){{ $("#{container}").tumblrReader({json}); }});</script>'
    return script.format(
        container=container,
        json=json.dumps({
             'blog': blog,
             'count': count,
             'tagged': tagged
        })
    )


@register.simple_tag
def tumblr_scripts():
    """
    Prints a ``<script></script>`` tag that includes Tumblr Reader javascript
    support.  Tumblr Reader javascript support must be included on any page
    using ``tumblr_posts``, but you can include it any way you like; see
    the ``tumblr_media_prefix`` template tag.
    
    Syntax::
    
        {% tumblr_scripts %}
    
    """
    return r'<script type="text/javascript" src="%sjquery.tumblr-reader.js"></script>' % django_settings.STATIC_URL

@register.simple_tag
def tumblr_styles():
    """
    Prints a <link></link> tag that includes some default Tumblr Reader styling.
    Using this CSS this is optional.
    
    Syntax::
    
        {% tumblr_styles %}
    
    """
    return r'<link rel="stylesheet" href="%sjquery.tumblr-reader.css" type="text/css" />' % django_settings.STATIC_URL

@register.simple_tag
def tumblr_static_url():
    """
    Prints the absolute URL of the Tumblr Reader static files directory; useful
    if you want to include Tumblr Reader javascript support in your site in
    a different way than using the ``tumblr_scripts`` template tag (for instance,
    asynchronously).

    Syntax::
    
        {% tumblr_static_url %}
    
    """
    return '%stumblr_reader/static/' % settings.STATIC_URL
