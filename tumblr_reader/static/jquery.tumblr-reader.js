var TumblrReader = {};
(function(){
    TumblrReader.createPost = function(post){
        var create = TumblrReader.createPost[post.type];
        if(!create){
            // TODO: this is an unsupported post type, should it get reported?
            return;
        }
        return create(post);
    };
    
    TumblrReader.createPost.regular = function(post){
        var template = '';
        template += '<div class="tumblr-reader-post tumblr-reader-post-regular">';
        template += '<div class="tumblr-reader-date"><a class="tumblr-reader-permalink" href="{url}">{date}</a></div>';
        template += '<div class="tumblr-reader-title">${title}</div>';
        template += '<div class="tumblr-reader-body">${body}</div>';
        template += '<div class="tumblr-reader-tags">${tags}</div>';
        template += '</div>'
        
        var params = {
            title: post['regular-title'],
            body: post['regular-body'],
            tags: post['tags'].join(', '),
            date: post['date'],
            url: post['url-with-slug'],
        };
        
        return $.tmpl(template, params);
    };
    
    TumblrReader.createPost.photo = function(post){
        var template = '';
        template += '<div class="tumblr-reader-post tumblr-reader-post-photo">';
        template += '<div class="tumblr-reader-date"><a class="tumblr-reader-permalink" href="{url}">{date}</a></div>';
        template += '<div class="tumblr-reader-photo"><img src="{photo}" /></div>';
        template += '<div class="tumblr-reader-caption">{caption}</div>';
        template += '<div class="tumblr-reader-tags">{tags}</div>';
        template += '</div>'
        
        var params = {
            caption: post['photo-caption'],
            photo: post['photo-url-1280'],
            tags: post['tags'].join(', '),
            date: post['date'],
            url: post['url-with-slug'],
        };
        
        return parse(template, params);
    };
    
    TumblrReader.createPost.quote = function(post){
        var template = '';
        template += '<div class="tumblr-reader-post tumblr-reader-post-quote">';
        template += '<div class="tumblr-reader-date"><a class="tumblr-reader-permalink" href="{url}">{date}</a></div>';
        template += '<div class="tumblr-reader-quote">{quote}</div>';
        template += '<div class="tumblr-reader-source">{source}</div>';
        template += '<div class="tumblr-reader-tags">{tags}</div>';
        template += '</div>'
        
        var params = {
            quote: post['quote-text'],
            source: post['quote-source'],
            tags: post['tags'].join(', '),
            date: post['date'],
            url: post['url-with-slug'],
        };
        
        return parse(template, params);
    };
    
    TumblrReader.createPost.link = function(post){
        var template = '';
        template += '<div class="tumblr-reader-post tumblr-reader-post-link">';
        template += '<div class="tumblr-reader-date"><a class="tumblr-reader-permalink" href="{url}">{date}</a></div>';
        template += '<div class="tumblr-reader-link"><a href="{url}">{text}</a></div>';
        template += '<div class="tumblr-reader-tags">{tags}</div>';
        template += '</div>'
        
        var params = {
            text: post['link-text'],
            url: post['link-url'],
            tags: post['tags'].join(', '),
            date: post['date'],
            url: post['url-with-slug'],
        };
        
        return parse(template, params);
    };
    
    TumblrReader.createPosts = function(posts){
        var $posts = [];
        for(var i = 0; i < posts.length; i++){
            $post = TumblrReader.createPost(posts[i]);
            if($post){
                $posts.append($post);
            }
        }
    };
    
    TumblrReader.createCallback = function(containerId){
        var $container;
        if(containerId){
            $container = $('#' + containerId);
        }
        else {
            // TODO: find the correct container.
            $container = $('body');
        }
        
        return function(blog){
            var $posts = TumblrReader.createPosts(blog.posts);
            $container.append($posts);
        };
    };
    
})();
