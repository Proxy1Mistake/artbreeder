class ObjectRandomJsonArt:
    def __init__(self, data):
        self.json = data
        self.key = []
        self.likes = []
        self.private = []
        self.prompt = []
        self.nsfw = []
        self.creator = []
        self.image_created_at = []
        self.creator_name = []
        self.liked = []
        self.downloaded = []
        self.tagged = []
        self.has_thumbnail = []
        self.time_string = []
        self.model_name = []
        self.size = []

    @property
    def object_random_json_art(self):
        try:
            for _ in self.json:
                self.key.append(_['key'])
                self.likes.append(_['likes'])
                self.private.append(_['private'])
                self.prompt.append(_['prompt'])
                self.nsfw.append(_['nsfw'])
                self.creator.append(_['creator'])
                self.image_created_at.append(_['image_created_at'])
                self.creator_name.append(_['creator_name'])
                self.liked.append(_['liked'])
                self.downloaded.append(_['downloaded'])
                self.tagged.append(_['tagged'])
                self.has_thumbnail.append(_['has_thumbnail'])
                self.time_string.append(_['time_string'])
                self.model_name.append(_['model_name'])
                self.size.append(_['size'])
        except(KeyError, TypeError): pass
        return self

class ObjectGetTheCreatorImages:
    def __init__(self, data):
        self.json = data
        self.id = []
        self.key = []
        self.private = []
        self.model = []
        self.creation_type = []
        self.creator = []
        self.created_at = []
        self.rand_id = []
        self.likes = []
        self.prompt = []
        self.nsfw = []
        self.prompt_ts = []
        self.metadata = []
        self.creator_name = []
        self.image_created_at = []
        self.model_display_name = []
        self.model_name = []
        self.liked = []
        self.downloaded = []
        self.tagged = []
        self.size = []

    @property
    def object_get_the_creator_images(self):
        try:
            for _ in self.json:
                self.id.append(_['id'])
                self.key.append(_['key'])
                self.private.append(_['private'])
                self.model.append(_['model'])
                self.creation_type.append(_['creation_type'])
                self.creator.append(_['creator'])
                self.created_at.append(_['created_at'])
                self.rand_id.append(_['rand_id'])
                self.likes.append(_['likes'])
                self.prompt.append(_['prompt'])
                self.nsfw.append(_['nsfw'])
                self.prompt_ts.append(_['prompt_ts'])
                self.metadata.append(_['metadata'])
                self.creator_name.append(_['creator_name'])
                self.image_created_at.append(_['image_created_at'])
                self.model_display_name.append(_['model_display_name'])
                self.model_name.append(_['model_name'])
                self.liked.append(_['liked'])
                self.downloaded.append(_['downloaded'])
                self.tagged.append(_['tagged'])
                self.size.append(_['size'])
        except(KeyError, TypeError): pass
        return self

class ObjectGetCreatorData:
    def __init__(self, data):
        self.json = data
        self.user = None
        self.username = None
        self.profile_image_key = None
        self.settings = None
        self.favorite_image_keys = None
        self.suspended = None
        self.num_followers = None
        self.num_following = None
        self.id = None
        self.socials = None
        self.subscription = None
        self.subscription_id = None
        self.subscription_plan = None
        self.subscription_plan_provider = None
        self.subscription_plan_cycle = None
        self.subscription_plan_ends_at = None
        self.subscription_plan_started_at = None
        self.subscription_plan_will_renew = None
        self.subscription_product = None
        self.subscription_product_order = None
        self.subscription_product_name = None
        self.subscription_product_display_name = None
        self.subscription_product_display_name_without_emoji = None
        self.subscription_product_price = None
        self.subscription_product_price_monthly = None
        self.subscription_product_price_yearly = None
        self.subscription_product_creditsPerMonth = None
        self.subscription_product_stripe = None
        self.subscription_product_stripe_yearly = None
        self.subscription_product_stripe_monthly = None
        self.subscription_product_paypal = None
        self.subscription_product_paypal_yearly = None
        self.subscription_product_paypal_monthly = None
        self.subscription_product_color = None
        self.subscription_product_colorClasses = None
        self.subscription_product_colorClasses_text = None
        self.subscription_product_colorClasses_background = None
        self.favorite_images = None
        self.favorite_Images_id = []
        self.favorite_images_key = []
        self.favorite_images_private = []
        self.favorite_images_model = []
        self.favorite_images_creation_type = []
        self.favorite_images_creator = []
        self.favorite_images_created_at = []
        self.favorite_images_rand_id = []
        self.favorite_images_likes = []
        self.favorite_images_prompt = []
        self.favorite_images_nsfw = []
        self.favorite_images_prompt_ts = []
        self.favorite_images_metadata = []
        self.favorite_images_creator_name = []
        self.favorite_images_created_at = []
        self.favorite_images_model_display_name = []
        self.favorite_images_model_name = []
        self.favorite_images_liked = []
        self.favorite_images_downloaded = []
        self.favorite_images_tagged = []
        self.favorite_images_size = []
        self.favorite_images_favorited = []

    @property
    def object_get_creator_data(self):
        try:
            self.user = self.json['user']
            self.username = self.json['user']['username']
            self.profile_image_key = self.json['user']['profileImageKey']
            self.settings = self.json['user']['settings']
            self.favorite_image_keys = self.json['user']['favoriteImageKeys']
            self.suspended = self.json['user']['suspended']
            self.favorite_image_keys = self.json['user']['favoriteImages']
            self.num_followers = self.json['user']['numFollowers']
            self.num_following = self.json['user']['numFollowing']
            self.id = self.json['user']['id']
            self.socials = self.json['user']['socials']
            self.subscription = self.json['user']['subscription']
            self.subscription_id = self.json['user']['subscription']['id']
            self.subscription_plan = self.json['user']['subscription']['plan']
            self.subscription_plan_provider = self.json['user']['subscription']['plan']['provider']
            self.subscription_plan_cycle = self.json['user']['subscription']['plan']['cycle']
            self.subscription_plan_ends_at = self.json['user']['subscription']['plan']['ends_at']
            self.subscription_plan_started_at = self.json['user']['subscription']['plan']['started_at']
            self.subscription_plan_will_renew = self.json['user']['subscription']['plan']['will_renew']
            self.subscription_product = self.json['user']['subscription']['product']
            self.subscription_product_order = self.json['user']['subscription']['product']['order']
            self.subscription_product_name = self.json['user']['subscription']['product']['name']
            self.subscription_product_display_name = self.json['user']['subscription']['product']['display_name']
            self.subscription_product_display_name_without_emoji = self.json['user']['subscription']['product']['display_name_without_emoji']
            self.subscription_product_price = self.json['user']['subscription']['product']['price']
            self.subscription_product_price_monthly = self.json['user']['subscription']['product']['price']['monthly']
            self.subscription_product_price_Yearly = self.json['user']['subscription']['product']['price']['yearly']
            self.subscription_product_creditsPerMonth = self.json['user']['subscription']['product']['creditsPerMonth']
            self.subscription_product_stripe = self.json['user']['subscription']['product']['stripe']
            self.subscription_product_stripe_yearly = self.json['user']['subscription']['product']['stripe']['yearly']
            self.subscription_product_stripe_monthly = self.json['user']['subscription']['product']['stripe']['monthly']
            self.subscription_product_paypal = self.json['user']['subscription']['product']['paypal']
            self.subscription_product_paypal_yearly = self.json['user']['subscription']['product']['paypal']['yearly']
            self.subscription_product_paypal_monthly = self.json['user']['subscription']['product']['paypal']['monthly']
            self.subscription_product_color = self.json['user']['subscription']['product']['color']
            self.subscription_product_colorClasses = self.json['user']['subscription']['product']['colorClasses']
            self.subscription_product_colorClasses_text = self.json['user']['subscription']['product']['colorClasses']['text']
            self.subscription_product_colorClasses_background = self.json['user']['subscription']['product']['colorClasses']['background']
            self.favorite_images = self.json['user']['favoriteImages']
            for _ in self.favorite_images:
                self.favorite_images_id.append(_['id'])
                self.favorite_image_keys.append(_['key'])
                self.favorite_images_private.append(_['private'])
                self.favorite_images_model.append(_['model'])
                self.favorite_images_creation_type.append(_['creation_type'])
                self.favorite_images_creator.append(_['creator'])
                self.favorite_images_created_at.append(_['created_at'])
                self.favorite_images_rand_id.append(_['rand_id'])
                self.favorite_images_likes.append(_['likes'])
                self.favorite_images_prompt.append(_['prompt'])
                self.favorite_images_prompt.append(_['nsfw'])
                self.favorite_images_prompt_ts.append(_['prompt_ts'])
                self.favorite_images_metadata.append(_['metadata'])
                self.favorite_images_creator_name.append(_['creator_name'])
                self.favorite_images_created_at.append(_['created_at'])
                self.favorite_images_model_display_name.append(_['model_display_name'])
                self.favorite_images_model_name.append(_['model_name'])
                self.favorite_images_liked.append(_['liked'])
                self.favorite_images_downloaded.append(_['downloaded'])
                self.favorite_images_tagged.append(_['tagged'])
                self.favorite_images_size.append(_['size'])
                self.favorite_images_favorited.append(_['favorited'])
        except(KeyError, TypeError): pass
        return self

class ObjectGetImageChildren:
    def __init__(self, data):
        self.json = data
        self.key = []
        self.likes = []
        self.private = []
        self.prompt = []
        self.nsfw = []
        self.creator = []
        self.image_created_at = []
        self.creator_name = []
        self.liked = []
        self.downloaded = []
        self.tagged = []
        self.has_thumbnail = []
        self.time_string = []
        self.model_name = []
        self.size = []

    @property
    def object_get_image_children(self):
        try:
            for _ in self.json:
                self.key.append(_['key'])
                self.likes.append(_['likes'])
                self.private.append(_['private'])
                self.prompt.append(_['prompt'])
                self.creator.append(_['creator'])
                self.image_created_at.append(_['image_created_at'])
                self.creator_name.append(_['creator_name'])
                self.liked.append(_['liked'])
                self.downloaded.append(_['downloaded'])
                self.tagged.append(_['tagged'])
                self.has_thumbnail.append(_['has_thumbnail'])
                self.time_string.append(_['has_thumbnail'])
                self.model_name.append(_['model_name'])
                self.size.append(_['size'])
        except(KeyError, TypeError): pass
        return self

