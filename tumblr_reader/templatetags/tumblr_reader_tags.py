from django.conf import settings
from django import template
from django.template import TemplateSyntaxError

register = template.Library()

class TumblrPostsNode(template.Node):
    def __init__(self, blog=None, count=None, tagged=None, callback=None):
        self.blog = block or settings.TUMBLR_READER_BLOG
        self.count = count or settings.TUMBLR_READER_COUNT
        self.callback = callback or settings.TUMBLR_READER_CALLBACK
        self.tagged = tagged or settings.TUMBLR_READER_TAGGED
    
    def render(self, context):
        return r"""
            <script type="text/javascript">var %s = TumblrReader.createCallback();</script>
            <script type="text/javascript" src="http://%s.tumblr.com/api/read/json?count=%s&tags=%s">
        """ % (callback, blog, count, tagged)

@register.simple_tag
def tumblr_posts(
    blog=settings.TUMBLR_READER_BLOG,
    count=settings.TUMBLR_READER_COUNT,
    tagged=settings.TUMBLR_READER_TAGGED,
    callback=settings.TUMBLR_READER_CALLBACK,
    container=settings.TUMBLR_READER_CONTAINER):
    """
    Embed posts from your Tumblr blog.
    
    Syntax:
    
        {% tumblr_posts %}
        {% tumblr_posts blog="blog" %}
        {% tumblr_posts count=10 %}
        {% tumblr_posts tagged="tag 1, tag 2" %}
        {% tumblr_posts callback="fn" %}
        {% tumblr_posts container="id" %}
    
    You can use any combination of these arguments, but you should use each
    not more than once.
    
    `from`:
        Defaults to `settings.TUMBLR_READER_BLOG`
        
    `count`:
        Defaults to `settings.TUMBLR_READER_COUNT`
        
    `tagged`:
        Defaults to `settings.TUMBLR_READER_TAGGED`

    `callback`:
        Defaults to `settings.TUMBLR_READER_CALLBACK`
        
        You shouldn't need to specify this unless you are embedding a blog
        or blogs multiple times on a single page; in that case you should be
        sure to use different callbacks for each embed:
        
            {% tumblr_posts callback="someCallback" %}
            {% tumblr_posts callback="anotherCallback" %}

    `container`:
        Defaults to `settings.TUMBLR_READER_CONTAINER`

        You shouldn't need to specify this unless you are embedding a blog
        or blogs multiple times on a single page; in that case you should
        be sure to use different container ids for each embed:
            
            {% tumblr_posts container="someId" %}
            {% tumblr_posts container="anotherId" %}
        
    """
    # Parsing
    try:
        count = int(count)
    except ValueError:
        raise TemplateSyntaxError('tumblr_posts: count must be an integer')
    
    return TumblrPostsNode(**{
        'blog': blog,
        'count': count,
        'tagged': tagged,
        'callback': callback,
        'container': container
    })
