class Bulletin:
    '''
    Bulletin class to define bulletin objects
    '''

    def __init__(self, id, title, description, urlToImage, content, publishedAt):
        self.id = id
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt
