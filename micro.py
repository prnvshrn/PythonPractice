import facebook, urllib3, requests, urllib

token = 'EAALBd0onih0BANOKHWOy1Vjc0YdVAvrP53tOlo1xDjH3upxJTnjTFQaqQIh5riDMrmksbPEPizcnZCfUf5sSolC9jZAnftthwWtZCni08E5JeBW7ChiXyY7bO6EgE1ar7vXxyPpyyn7qz7Le8ktVJVbr9NRL8OSMLmZCZBHD2B6enq9o8EgWRIlZC1cwvFZCjPvnRTt2uiGfAZDZD'

def init():
    graph = facebook.GraphAPI(access_token=token, version = 2.8)
    #events = graph.request('/search?q=Poetry&type=event&limit=10000')
    events = graph.request('/me/photos')
    eventList = events['data']
    print(events)

def swapi():
    #http swapi.co/api/planets/1/
    response = requests.get('https://swapi.co/api/planets/1/').json()
    for key, value in response.items():
        print(key,':',value)

if __name__ == '__main__':
    swapi()