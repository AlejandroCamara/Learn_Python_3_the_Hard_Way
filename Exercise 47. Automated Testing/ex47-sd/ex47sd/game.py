# Exercise 47. Automated Testing - Study Drills

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
    
    def delete_path(self, path):
        self.paths.pop(path, None)

