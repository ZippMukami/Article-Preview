from urllib import response


class Bulletin:
    '''
    Bulletin class to define Bulletin Objects
    '''

    def __init__(self, id, title, description, urlToImage, content, publishedAt):
        self.id = id
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt

class Review:

    all_reviews = []
    
    def __init__(self, id, title, urlToImage, review):
        self.id = id
        self.title = title
        self.urlToImage = urlToImage
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
      Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.id == id:
                response.append(review)

        return response