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