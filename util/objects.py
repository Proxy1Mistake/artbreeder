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

class getTheCreatorImages:
    def __init__(self, data):
        self.json = data
        self.id = []
        self.key = []
        self.private = []
        self.model = []
        self.creationType = []
        self.creator = []
        self.createdAt = []
        self.randId = []
        self.likes = []
        self.prompt = []
        self.nsfw = []
        self.promptTs = []
        self.metadata = []
        self.creatorName = []
        self.imageCreatedAt = []
        self.modelDisplayName = []
        self.modelName = []
        self.liked = []
        self.downloaded = []
        self.tagged = []
        self.size = []

    @property
    def getTheCreatorImages(self):
        for x in self.json:
            try: self.id.append(x['id'])
            except(KeyError, TypeError): pass
            try: self.key.append(x['key'])
            except(KeyError, TypeError): pass
            try: self.private.append(x['private'])
            except(KeyError, TypeError): pass
            try: self.model.append(x['model'])
            except(KeyError, TypeError): pass
            try: self.creationType.append(x['creation_type'])
            except(KeyError, TypeError): pass
            try: self.creator.append(x['creator'])
            except(KeyError, TypeError): pass
            try: self.createdAt.append(x['created_at'])
            except(KeyError, TypeError): pass
            try: self.randId.append(x['rand_id'])
            except(KeyError, TypeError): pass
            try: self.likes.append(x['likes'])
            except(KeyError, TypeError): pass
            try: self.prompt.append(x['prompt'])
            except(KeyError, TypeError): pass
            try: self.nsfw.append(x['nsfw'])
            except(KeyError, TypeError): pass
            try: self.promptTs.append(x['prompt_ts'])
            except(KeyError, TypeError): pass
            try: self.metadata.append(x['metadata'])
            except(KeyError, TypeError): pass
            try: self.creatorName.append(x['creator_name'])
            except(KeyError, TypeError): pass
            try: self.imageCreatedAt.append(x['image_created_at'])
            except(KeyError, TypeError): pass
            try: self.modelDisplayName.append(x['model_display_name'])
            except(KeyError, TypeError): pass
            try: self.modelName.append(x['model_name'])
            except(KeyError, TypeError): pass
            try: self.liked.append(x['liked'])
            except(KeyError, TypeError): pass
            try: self.downloaded.append(x['downloaded'])
            except(KeyError, TypeError): pass
            try: self.tagged.append(x['tagged'])
            except(KeyError, TypeError): pass
            try: self.size.append(x['size'])
            except(KeyError, TypeError): pass
        return self

class getСreatorData:
    def __init__(self, data):
        self.json = data
        self.user = None
        self.username = None
        self.profileImageKey = None
        self.settings = None
        self.favoriteImageKeys = None
        self.suspended = None
        self.favoriteImageKeys = None
        self.numFollowers = None
        self.numFollowing = None
        self.id = None
        self.socials = None
        self.subscription = None
        self.subscriptionId = None
        self.subscriptionPlan = None
        self.subscriptionPlanProvider = None
        self.subscriptionPlanCycle = None
        self.subscriptionPlanEndsAt = None
        self.subscriptionPlanStartedAt = None
        self.subscriptionPlanWillRenew = None
        self.subscriptionProduct = None
        self.subscriptionProductOrder = None
        self.subscriptionProductName = None
        self.subscriptionProductDisplayName = None
        self.subscriptionProductDisplayNameWithoutEmoji = None
        self.subscriptionProductPrice = None
        self.subscriptionProductPriceMonthly = None
        self.subscriptionProductPriceYearly = None
        self.subscriptionProductCreditsPerMont = None
        self.subscriptionProductStripe = None
        self.subscriptionProductStripeYearly = None
        self.subscriptionProductStripeMonthly = None
        self.subscriptionProductPaypal = None
        self.subscriptionProductPaypalYearly = None
        self.subscriptionProductPaypalMonthly = None
        self.subscriptionProductColor = None
        self.subscriptionProductColorClasses = None
        self.subscriptionProductColorClassesText = None
        self.subscriptionProductColorClassesBackground = None
        self.favoriteImageId = []
        self.favoriteImageKey = []
        self.favoriteImagePrivate = []
        self.favoriteImageModel = []
        self.favoriteImageCreationType = []
        self.favoriteImageCreator = []
        self.favoriteImageCreatedAt = []
        self.favoriteImageRandId = []
        self.favoriteImageLikes = []
        self.favoriteImagePrompt = []
        self.favoriteImageNsfw = []
        self.favoriteImagePromptTs = []
        self.favoriteImageMetadata = []
        self.favoriteImageCreatorName = []
        self.favoriteImageCreatedAt = []
        self.favoriteImageModelDisplayName = []
        self.favoriteImageModelName = []
        self.favoriteImageLiked = []
        self.favoriteImageDownloaded = []
        self.favoriteImageTagged = []
        self.favoriteImageSize = []
        self.favoriteImageFavorited = []

    @property
    def getСreatorData(self):
        try: self.user = self.json['user']
        except(KeyError, TypeError): pass
        try: self.username = self.json['user']['username']
        except(KeyError, TypeError): pass
        try: self.profileImageKey = self.json['user']['profileImageKey']
        except(KeyError, TypeError): pass
        try: self.settings = self.json['user']['settings']
        except(KeyError, TypeError): pass
        try: self.favoriteImageKeys = self.json['user']['favoriteImageKeys']
        except(KeyError, TypeError): pass
        try: self.suspended = self.json['user']['suspended']
        except(KeyError, TypeError): pass
        try: self.favoriteImages = self.json['user']['favoriteImages']
        except(KeyError, TypeError): pass
        try: self.numFollowers = self.json['user']['numFollowers']
        except(KeyError, TypeError): pass
        try: self.numFollowing = self.json['user']['numFollowing']
        except(KeyError, TypeError): pass
        try: self.id = self.json['user']['id']
        except(KeyError, TypeError): pass
        try: self.socials = self.json['user']['socials']
        except(KeyError, TypeError): pass
        try: self.subscription = self.json['user']['subscription']
        except(KeyError, TypeError): pass
        try: self.subscriptionId = self.json['user']['subscription']['id']
        except(KeyError, TypeError): pass
        try: self.subscriptionPlan = self.json['user']['subscription']['plan']
        except(KeyError, TypeError): pass
        try: self.subscriptionPlanProvider = self.json['user']['subscription']['plan']['provider']
        except(KeyError, TypeError): pass
        try: self.subscriptionPlanCycle = self.json['user']['subscription']['plan']['cycle']
        except(KeyError, TypeError): pass
        try: self.subscriptionPlanEndsAt = self.json['user']['subscription']['plan']['ends_at']
        except(KeyError, TypeError): pass
        try: self.subscriptionPlanStartedAt = self.json['user']['subscription']['plan']['started_at']
        except(KeyError, TypeError): pass
        try: self.subscriptionPlanWillRenew = self.json['user']['subscription']['plan']['will_renew']
        except(KeyError, TypeError): pass
        try: self.subscriptionProduct = self.json['user']['subscription']['product']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductOrder = self.json['user']['subscription']['product']['order']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductName = self.json['user']['subscription']['product']['name']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductDisplayName = self.json['user']['subscription']['product']['display_name']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductDisplayNameWithoutEmoji = self.json['user']['subscription']['product']['display_name_without_emoji']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductPrice = self.json['user']['subscription']['product']['price']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductPriceMonthly = self.json['user']['subscription']['product']['price']['monthly']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductPriceYearly = self.json['user']['subscription']['product']['price']['yearly']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductCreditsPerMont = self.json['user']['subscription']['product']['creditsPerMonth']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductStripe = self.json['user']['subscription']['product']['stripe']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductStripeYearly = self.json['user']['subscription']['product']['stripe']['yearly']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductStripeMonthly = self.json['user']['subscription']['product']['stripe']['monthly']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductPaypal = self.json['user']['subscription']['product']['paypal']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductPaypalYearly = self.json['user']['subscription']['product']['paypal']['yearly']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductPaypalMonthly = self.json['user']['subscription']['product']['paypal']['monthly']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductColor = self.json['user']['subscription']['product']['color']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductColorClasses = self.json['user']['subscription']['product']['colorClasses']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductColorClassesText = self.json['user']['subscription']['product']['colorClasses']['text']
        except(KeyError, TypeError): pass
        try: self.subscriptionProductColorClassesBackground = self.json['user']['subscription']['product']['colorClasses']['background']
        except(KeyError, TypeError): pass
        for x in self.favoriteImages:
            try: self.favoriteImageId.append(x['id'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageKey.append(x['key'])
            except(KeyError, TypeError): pass
            try: self.favoriteImagePrivate.append(x['private'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageModel.append(x['model'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageCreationType.append(x['creation_type'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageCreator.append(x['creator'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageCreatedAt.append(x['created_at'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageRandId.append(x['rand_id'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageLikes.append(x['likes'])
            except(KeyError, TypeError): pass
            try: self.favoriteImagePrompt.append(x['prompt'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageNsfw.append(x['nsfw'])
            except(KeyError, TypeError): pass
            try: self.favoriteImagePromptTs.append(x['prompt_ts'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageMetadata.append(x['metadata'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageCreatorName.append(x['creator_name'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageCreatedAt.append(x['image_created_at'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageModelDisplayName.append(x['model_display_name'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageModelName.append(x['model_name'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageLiked.append(x['liked'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageDownloaded.append(x['downloaded'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageTagged.append(x['tagged'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageSize.append(x['size'])
            except(KeyError, TypeError): pass
            try: self.favoriteImageFavorited.append(x['favorited'])
            except(KeyError, TypeError): pass
        return self

