---
layout: post
title: Computing Bacon Numbers
---

I spent the past week doing Google Foobar exercises, and that was really fun (and really addictive). I managed to stop doing that to start working on a fun project: calculating a given person's [Bacon number](http://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon#Bacon_numbers).

### First version

My first idea was to parse [IMDb](http://www.imdb.com/) pages to extract the information I would need. I discovered [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/), which is amazing and super easy to use. To find out what movies an actor was in all I needed to do was search for /title/ in that actor's IMDb page, and to find what actors were in a movie I searched for /name/, and it works! After 2 days of working in this version, I had a Command Line Interface that could tell if an actor's Bacon number was 1 or greater.

{% highlight python%}
import urllib2
import re
from BeautifulSoup import BeautifulSoup

def find_movies(actor_url):
    """
    Function that receives an actor m.imdb url and returns urls for all the movies 
    the actor was in
    """
    page = urllib2.urlopen(actor_url)
    data = page.read()
    soup = BeautifulSoup(data)
    movies = []

    for link in soup.findAll('a', href = re.compile('/title/')):
        movies.append(("http://m.imdb.com" + str(link.get('href'))))

    return movies

def find_actors(movie_url): 
    actors = []
    page = urllib2.urlopen(movie_url)
    data = page.read()
    soup = BeautifulSoup(data)

    for link in soup.findAll('a', href = re.compile('http://m.imdb.com/name/nm')):
        actors.append(str(link.get('href')[:33]))

    return actors

def get_neighbors(actor_url):
    neighbors = []
    for movie in find_movies(actor_url):
        actors = find_actors(movie)
        for x in actors:
            if x not in neighbors:
                neighbors.append(x)
    return neighbors

def get_graph(actors_urls):
    graph = {}
    for actor in actors_urls:
        print actor
        graph[actor] = get_neighbors(actor)
    return graph

Bacon = "http://m.imdb.com/name/nm0000102/filmotype/actor?ref_=m_nmfm_1"

def bacon_identifier_function(actor_url, graph):
    if actor_url in graph[Bacon]:
        return "1"
    else:
        return "Bigger than 1"

grafo = get_graph([Bacon] + get_neighbors(Bacon))
 
# Command Line Interface
while True:
    actor = raw_input("Please insert an actor imdb identifier, or q to quit ")
    if actor == "q":
        break
    print bacon_identifier_function("http://m.imdb.com/name/" + actor + "/", grafo)

{% endhighlight %}

But this version was just too slow to do anything other than telling if someone did a movie with Kevin Bacon or not.

## Final version

Turns out IMDb lets a subset of its data available as plain [text files](http://www.imdb.com/interfaces), and everything I needed was in there. So I could create my graph by parsing text files. At first I was trying to have a graph a just the actors, and 2 actors were connected if they'd done a movie together. To do that I would have to look at every pair of actors and connect them if they have a movie in common. But I don't need the graph to be this way in order to calculate someone's Bacon number. If I have a graph in which an actor is connected to every movie he made and a movie is connected to every actor in it, the shortest path between an actor and Kevin Bacon will be twice that actor's Bacon number. And I can generate this graph in a couple minutes.

### Finding the shortest path

So now all I have to do is find the shortest path between 2 nodes in a graph. Since all edges have the same weight, I can solve this with a [Breadth-First Search](http://www.eecs.yorku.ca/course_archive/2006-07/W/2011/Notes/BFS_part2.pdf):
{% highlight python%}
def BFS(graph, source):
    line = deque()
    distance = {source : 0}
    line.append(source)
    while line:
        t = line.popleft()
        for e in graph[t]:
            if e not in distance:
                distance[e] = distance[t] + 1
                line.append(e)
    return distance
{% endhighlight %}
So if I pass to BFS my graph with all the actors and movies and source = Bacon, I get a dictionary:
{% highlight python%}
doubled_bacon_numbers = BFS(graph, Bacon)
{% endhighlight %}
And a someone's Bacon number is just: 
{% highlight python%}
doubled_bacon_numbers[someone]/2
{% endhighlight %}

The final version of my code is [here](https://github.com/adusca/bacon-number/blob/master/file_parser.py)
