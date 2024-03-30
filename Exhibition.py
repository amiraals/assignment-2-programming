class Artwork:
    """Class to represent an artwork in the museum"""

    def __init__(self, title, artist, creation_date):
        # Initializing artwork attributes
        self.title = title
        self.artist = artist
        self.creation_date = creation_date


class Exhibition:
    """Class to represent an exhibition that includes multiple artworks

    This class has an aggregation relationship with the Artwork class"""
    def __init__(self, name, artworks=[]):
        # Initializing exhibition attributes
        self.name = name
        self.artworks = artworks # This parameter allows for the possibility of passing a list of Artwork objects when creating an Exhibition object

    def add_artwork(self, artwork):
        # Adding an artwork to the exhibition
        self.artworks.append(artwork)

    def remove_artwork(self, title):
        for artwork in self.artworks:
            if artwork.title == title:
                self.artworks.remove(artwork)
                return True  # Artwork found and removed
        return False  # Artwork not found

    def display_info(self):
        # Displaying information about the exhibition and its artworks
        print(f"Exhibition: {self.name}")
        for artwork in self.artworks:
            print(f"Artwork: {self.artworks.index(artwork) + 1}. {artwork.title}, Artist: {artwork.artist}, Date: {artwork.creation_date}")


"""
The Artwork class details individual pieces of art within the museum, 
while the Exhibition class manages collections of artworks. they have 
an aggregation relationship, where an Exhibition can contain multiple 
Artwork objects but does not own them outright, allowing artworks to 
exist independently outside of any specific exhibition. 
"""
