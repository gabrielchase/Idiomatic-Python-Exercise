import urllib.request  as urllib2 


class ConnectionError(Exception):
    # print('Connection Error')
    pass

class UnknownError(Exception):
    # print('Unknown Error')
    pass

def get_http_header(url, header_name):
    """Given an HTTP(S) URL, return the value of the header.
    If the header does not exist, return None.
    Do not follow redirects.
    Raise ConnectionError for connection-related errors.
    Raise UnknownError for other types of errors.
    """

    try:
        response = urllib2.urlopen(url)
        
        if response.info().get(header_name):
            return None
            
    except ConnectionError:
        print('Connection Error')
    except UnknownError: 
        print('Unknown Error')


print(get_http_header('https://www.google.com.ph/?gfe_rd=cr&ei=LpiWWazUNYqBvATnhaiYCA&gws_rd=ssl', 'Cache-Control'))
print(get_http_header('https://www.google.com.ph/?gfe_rd=cr&ei=LpiWWazUNYqBvATnhaiYCA&gws_rd=ssl', 'Content-Type'))
print(get_http_header('https://www.google.com.ph/?gfe_rd=cr&ei=LpiWWazUNYqBvATnhaiYCA&gws_rd=ssl', 'Server'))

print(get_http_header('https://www.skdfjalsdfsdalsjdf.com', 'Cache-Control'))