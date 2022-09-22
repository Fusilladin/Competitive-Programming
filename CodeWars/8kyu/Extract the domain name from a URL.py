def domain_name(url):
    #print(url,'start')
    url = url.split('//')
    if len(url) == 1:
        url = url[0].split('.')
        if 'www' in url:
            url = url[1]
        else:
            url = url[0]
        return url
    else:
        url = url[1].split('.')
        if 'www' in url: 
            url = url[1]
        else:
            url = url[0]
    return url
