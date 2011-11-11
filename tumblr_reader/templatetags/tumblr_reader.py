from .. import settings
from django import template
from django.template import TemplateSyntaxError

register = template.Library()

class TumblrPostsNode(template.Node):
    def __init__(self, blog=None, count=None, tagged=None, callback=None):
        # Default to settings in case we want to use this node from a
        # different tag.
        self.blog = block or settings.BLOG
        self.count = count or settings.COUNT
        self.callback = callback or settings.CALLBACK
        self.tagged = tagged or settings.TAGGED
    
    def render(self, context):
        return r"""
            <script type="text/javascript">var %s = TumblrReader.createCallback("%s");</script>
            <script type="text/javascript" src="http://%s.tumblr.com/api/read/json?callback=%s&count=%s&tags=%s">
        """ % (callback, container, blog, callback, count, tagged)

@register.simple_tag
def tumblr_posts(
    blog=settings.BLOG,
    count=settings.COUNT,
    tagged=settings.TAGGED,
    callback=settings.CALLBACK,
    container=settings.CONTAINER):
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
    
    return r"""
            <script type="text/javascript">var %s = TumblrReader.createCallback("%s");</script>
            <script type="text/javascript" src="http://%s.tumblr.com/api/read/json?callback=%s&count=%s&tags=%s">
        """ % (callback, container, blog, callback, count, tagged)

    return TumblrPostsNode(**{
        'blog': blog,
        'count': count,
        'tagged': tagged,
        'callback': callback,
        'container': container
    })

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
    return r'<script type="text/javascript" src="%sjquery.tumblr-reader.js"></script>' % settings.MEDIA_URL

@register.simple_tag
def tumblr_media_url():
    """
    Prints the value of `settings.TUMBLR_READER_MEDIA_URL` setting; useful
    if you want to include Tumblr Reader javascript support in your site in
    a different way than using {% tumblr_scripts %} (for instance,
    asynchronously).

    Syntax:
    
        {% tumblr_media_url %}
    
    """
    return settings.MEDIA_URL
