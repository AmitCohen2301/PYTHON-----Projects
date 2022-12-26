import re
fileName = 'movies.txt'

def readMovies (fileNameToRead):
    actorsDict = {}
    file = open(fileNameToRead,"r")
    lines = file.readlines()
    for line in lines: # Move on every line in file
        valuesInLine = line.split(',')
        valuesInLine[len(valuesInLine)-1] = valuesInLine[len(valuesInLine)-1].replace('\n','') # Delete the at the end of line \n
        actorsDict[valuesInLine[0]] = (valuesInLine[1:]) # Add the actor and movies to dict
    return actorsDict

def playedWith (actor):
    actorsDict = readMovies(fileName)
    actorsThatActorPlayedWith = []
    for movie in actorsDict[actor]: # Move on all movies the actor played in
        for otherActor in actorsDict: # Move on all actors to check if played in the same movie
            if otherActor == actor: # The same actor we check
                continue
            if movie in actorsDict[otherActor]: # Check if played in the same movie
                actorsThatActorPlayedWith.append((otherActor, movie))
    return actorsThatActorPlayedWith

def find(pattern):
    moviesListThatPrinted = []
    actorsDict = readMovies(fileName)
    regExp = re.compile(pattern)
    print('Actors:')
    for actor in actorsDict: # Move on all actors
        res = regExp.findall(actor) # Split to sub string if they answer the reg exp
        if len(res) > 0: # Check if reg exp is in the actor name
            print(f'\t{actor}')
    print('Movies:')
    for actor in actorsDict: # Move on all actors
        for movie in actorsDict[actor]: # Move on all movies the actor played in
            res = regExp.findall(movie) # Split to sub string if they answer the reg exp
            if len(res) > 0:
                if movie not in moviesListThatPrinted: # Check if we alredy print the movie
                    moviesListThatPrinted.append(movie)
                    print(f'\t{movie}')