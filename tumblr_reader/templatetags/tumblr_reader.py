import json

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
    
    Syntax:
    
        {% tumblr_posts %}
        {% tumblr_posts blog="blog" %}
        {% tumblr_posts count=10 %}
        {% tumblr_posts tagged="tag 1, tag 2" %}
        {% tumblr_posts container="id" %}
    
    You can use any combination of these arguments, but you should use each
    not more than once.
    
    `from`:
        Defaults to `settings.TUMBLR_READER_BLOG`
        
    `count`:
        Defaults to `settings.TUMBLR_READER_COUNT`
        
    `tagged`:
        Defaults to `settings.TUMBLR_READER_TAGGED`

    `container`:
        Defaults to `settings.TUMBLR_READER_CONTAINER`

        You shouldn't need to specify this unless you are embedding a blog
        or blogs multiple times on a single page; in that case you almost
        certainly want to use different container ids for each embed:
            
            {% tumblr_posts container="someId" %}
            {% tumblr_posts container="anotherId" %}
        
    """
    # Not strictly necessary, just here to catch errors earlier.
    try:
        count = int(count)
    except ValueError:
        raise TemplateSyntaxError('tumblr_posts: count must be an integer')
    
    script = '<script type="text/javascript">$.tumblrReader.read({json});</script>'
    return script.format(
        json=json.dumps({
             'blog': blog
             'count': count,
             'container': container,
             'tagged': tagged
        })
    )


@register.simple_tag
def tumblr_scripts():
    """
    Prints a <script></script> tag that includes Tumblr Reader javascript
    support.  Tumblr Reader javascript support must be included on any page
    using {% tumblr_posts %}, but you can include it any way you like; see
    {% tumblr_media_prefix %}.
    
    Syntax:
    
        {% tumblr_scripts %}
    
    """
    return r'<script type="text/javascript" src="%sjquery.tumblr-reader.js"></script>' % settings.MEDIA_PREFIX

@register.simple_tag
def tumblr_styles():
    """
    Prints a <link></link> tag that includes some default Tumblr Reader styling.
    This is optional.
    
    Syntax:
    
        {% tumblr_styles %}
    
    """
    return r'<link rel="stylesheet" href="%jquery.tumblr-reader.css" type="text/css" />' % settings.MEDIA_PREFIX

@register.simple_tag
def tumblr_media_prefix():
    """
    Prints the value of `settings.TUMBLR_READER_MEDIA_PREFIX` setting; useful
    if you want to include Tumblr Reader javascript support in your site in
    a different way than using {% tumblr_scripts %} (for instance,
    asynchronously).

    Syntax:
    
        {% tumblr_media_prefix %}
    
    """
    return settings.MEDIA_PREFIX
