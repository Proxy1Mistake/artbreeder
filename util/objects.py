class randomJsonArt:
    def __init__(self, data):
        self.json = data
        self.key = []
        self.likes = []
        self.private = []
        self.prompt = []
        self.nsfw = []
        self.creator = []
        self.imageCreatedAt = []
        self.creatorName = []
        self.liked = []
        self.downloaded = []
        self.tagged = []
        self.hasThumbnail = []
        self.timeString = []
        self.modelName = []
        self.size = []

    @property
    def randomJsonArt(self):
        for x in self.json:
            try: self.key.append(x['key'])
            except(KeyError, TypeError): pass
            try: self.likes.append(x['likes'])
            except(KeyError, TypeError): pass
            try: self.private.append(x['private'])
            except(KeyError, TypeError): pass
            try: self.prompt.append(x['prompt'])
            except(KeyError, TypeError): pass
            try: self.nsfw.append(x['nsfw'])
            except(KeyError, TypeError): pass
            try: self.creator.append(x['creator'])
            except(KeyError, TypeError): pass
            try: self.imageCreatedAt.append(x['image_created_at'])
            except(KeyError, TypeError): pass
            try: self.creatorName.append(x['creator_name'])
            except(KeyError, TypeError): pass
            try: self.liked.append(x['liked'])
            except(KeyError, TypeError): pass
            try: self.downloaded.append(x['downloaded'])
            except(KeyError, TypeError): pass
            try: self.tagged.append(x['tagged'])
            except(KeyError, TypeError): pass
            try: self.hasThumbnail.append(x['has_thumbnail'])
            except(KeyError, TypeError): pass
            try: self.timeString.append(x['time_string'])
            except(KeyError, TypeError): pass
            try: self.modelName.append(x['model_name'])
            except(KeyError, TypeError): pass
            try: self.size.append(x['size'])
            except(KeyError, TypeError): pass
        return self
