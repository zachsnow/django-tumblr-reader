====================
Django Tumblr Reader
====================

Django Tumblr Reader is a simple Django application that defines template tags
for embedding your Tumblr blog in your Django website.  An example of Django
Tumblr Reader in action can be found at::

    http://zachsnow.com/demos/django-tumblr-reader/

Installation
------------

**NOTE** Django Tumblr Reader requires Django *trunk* (in particular it depends
on recent upgrades to the ``simple_tag`` template tag helper).  So first grab
that::
    
    svn co https://code.djangoproject.com/svn/django/trunk/
    
Alternatively, install it with ``pip``::

    pip install -e svn+https://code.djangoproject.com/svn/django/trunk/

To install Django Tumblr Reader, grab the source::

    hg clone https://bitbucket.org/zachsnow/django-tumblr-reader

Alternatively, install it with ``pip``::

    pip install -e hg+https://bitbucket.org/zachsnow/django-tumblr-reader/

Then just add ``tumblr_reader`` to your ``INSTALLED_APPS``, and be sure that in
production your serve ``django-tumblr-reader/tumblr_reader/static/``; for more
information check out the ``django.contrib.staticfiles`` application.  For testing
with the debug server you just need to make sure that you have
``django.contrib.staticfiles`` in your ``INSTALLED_APPS``.

Django Tumblr Reader is really just a lightweight wrapper around
jquery.tumblr-reader.js, which comes packaged with Django Tumblr Reader,
and which can be easily used without Django.
 
Usage
-----

The primary way of using Django Tumblr Reader is through the ``tumblr_posts``
template tag::

    {% load tumblr_reader %}
    
    {% tumblr_posts %}

There are a number of optional arguments; all of these are taken to be
as defined in the settings, described below, by default.  To retrieve
posts from a specific blog::

    {% tumblr_posts blog='some-blog' %}
    
To retrieve a specific number of posts::

    {% tumblr_posts count=32 %}
    
To retrieve posts having a particular tag (note that, due to limitations of
the Tumblr API version 1, you can only specify a single tag on which to
filter)::

    {% tumblr_posts tagged="beer" %}
    
To write the retrieved posts into a particular container, by id::

    {% tumblr_posts container="a-random-element" %}
    
All of the above options can be specified in any combination, but may
only be specified once::

    {% tumblr_posts blog="delicious-brews" tagged="ipa" container="ipas" count=100 %}

To make it easier to include jquery.tumblr-reader.js and jquery.tumblr-reader.css
there are two additional template tags::

    {% tumblr_scripts %}
    {% tumblr_styles %}
    
These render ``<script></script>`` and ``<style></style>`` tags for those files,
based on the value of ``settings.TUMBLR_READER_MEDIA_PREFIX``.

Finally, if you for some reason need access to the value of
``settings.TUMBLR_READER_MEDIA_PREFIX`` from within a template (perhaps to load
jquery.tumblr-reader.js asynchronously) you can use::

    {% tumblr_media_prefix %}

Settings
--------

``TUMBLR_READER_BLOG``
    
    Tumblr blog to embed in your site; you should change this to your blog.
    For instance, if your blog is at ``http://iheartdjango.tumblr.com`` you
    should set this to ``"iheartdjango"``.
    
    This is the default blog embedded by the ``tumblr_posts`` template tag.
    The default value is ``"django-tumblr-reader"``. 

``TUMBLR_READER_COUNT``

    This is the default number of posts that will be embedded by the
    ``tumblr_posts`` template tag.  The default is 10.

``TUMBLR_READER_TAGGED``

    Posts with this tag will be embedded by the ``tumblr_posts`` template tag
    by default.  The default value is ``""``, which means that all posts will be
    embedded.

``TUMBLR_READER_CONTAINER``
    
    The default container id into which posts embedded by the ``tumblr_posts``
    template tag should be written; the default is the empty string, which means
    that posts will be written into the same container as the template tag.
 
``TUMBLR_READER_MEDIA_PREFIX``
    
    The url prefix at which Tumblr Reader static files will be served;
    defaults to ``os.path.join(settings.MEDIA_URL, "/tumblr-reader/")``.

Rendering
---------

By default jquery.tumblr-reader.js renders simple, structured HTML with lots
of CSS classes for easy styling (see jquery.tumblr-reader.css for an example
the details all of these classes).  However, if this structure does not meet your
needs, it can be easily overridden.

Each type of Tumblr post has a corresponding entry in the ``$.fn.tumblrReader.parsers``
dictionary.  These entries are parsing functions that take a JSON representation
of a Tumblr post and return a jQuery object or DOM node.  For instance, to 
change how the "photo" type of post is rendered::

    $.fn.tumblrReader.parsers.photo = function(post){
        var $post = $("<h1>OH HAI I'M A PHOTO!"</h1>);
        return $post;
    };
    
The Tumblr post types that are currently supported are *regular*, *quote*,
*link*, *photo*, and *conversation*.  **Not supported** are types *audio*
and *video*.  If there are other types you need to support (or if
Tumblr adds new ones) simply add a parser for that type.

In addition, a few "sub-parsers" are used by the default post parsers, they
are ``$.fn.tumblrReader.parsers.date`` and ``$.fn.tumblrReader.parsers.tags``. 
If all you want to change is how those components of every post are rendered by default,
simply override those parsers.  These parsers also take a JSON representation of
a post, but should only render the date and tags, respectively.

Finally, the "sub-parser" ``$.fn.tumblrReader.parsers.phrase`` is used to
render each phrase in a conversation; it takes an individual phrase, not an
entire post.

I'm not too happy with how rendering works, but it gets the job done for my
current use cases.

Contact
-------
Feel free to contact me about Django Tumblr Reader::

    z@zachsnow.com
    @therealzachsnow
