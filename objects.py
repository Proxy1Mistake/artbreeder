class obj_random_json_art:
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
    def obj_random_json_art(self):
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
            try: self.image_created_at.append(x['image_created_at'])
            except(KeyError, TypeError): pass
            try: self.creator_name.append(x['creator_name'])
            except(KeyError, TypeError): pass
            try: self.liked.append(x['liked'])
            except(KeyError, TypeError): pass
            try: self.downloaded.append(x['downloaded'])
            except(KeyError, TypeError): pass
            try: self.tagged.append(x['tagged'])
            except(KeyError, TypeError): pass
            try: self.has_thumbnail.append(x['has_thumbnail'])
            except(KeyError, TypeError): pass
            try: self.time_string.append(x['time_string'])
            except(KeyError, TypeError): pass
            try: self.model_name.append(x['model_name'])
            except(KeyError, TypeError): pass
            try: self.size.append(x['size'])
            except(KeyError, TypeError): pass
        return self

class obj_get_the_creator_images:
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
    def obj_get_the_creator_images(self):
        for x in self.json:
            try: self.id.append(x['id'])
            except(KeyError, TypeError): pass
            try: self.key.append(x['key'])
            except(KeyError, TypeError): pass
            try: self.private.append(x['private'])
            except(KeyError, TypeError): pass
            try: self.model.append(x['model'])
            except(KeyError, TypeError): pass
            try: self.creation_type.append(x['creation_type'])
            except(KeyError, TypeError): pass
            try: self.creator.append(x['creator'])
            except(KeyError, TypeError): pass
            try: self.created_at.append(x['created_at'])
            except(KeyError, TypeError): pass
            try: self.rand_id.append(x['rand_id'])
            except(KeyError, TypeError): pass
            try: self.likes.append(x['likes'])
            except(KeyError, TypeError): pass
            try: self.prompt.append(x['prompt'])
            except(KeyError, TypeError): pass
            try: self.nsfw.append(x['nsfw'])
            except(KeyError, TypeError): pass
            try: self.prompt_ts.append(x['prompt_ts'])
            except(KeyError, TypeError): pass
            try: self.metadata.append(x['metadata'])
            except(KeyError, TypeError): pass
            try: self.creator_name.append(x['creator_name'])
            except(KeyError, TypeError): pass
            try: self.image_created_at.append(x['image_created_at'])
            except(KeyError, TypeError): pass
            try: self.model_display_name.append(x['model_display_name'])
            except(KeyError, TypeError): pass
            try: self.model_name.append(x['model_name'])
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

class obj_get_creator_data:
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
    def obj_get_creator_data(self):
        try: self.user = self.json['user']
        except(KeyError, TypeError): pass
        try: self.username = self.json['user']['username']
        except(KeyError, TypeError): pass
        try: self.profile_image_key = self.json['user']['profileImageKey']
        except(KeyError, TypeError): pass
        try: self.settings = self.json['user']['settings']
        except(KeyError, TypeError): pass
        try: self.favorite_image_keys = self.json['user']['favoriteImageKeys']
        except(KeyError, TypeError): pass
        try: self.suspended = self.json['user']['suspended']
        except(KeyError, TypeError): pass
        try: self.favorite_image_keys = self.json['user']['favoriteImages']
        except(KeyError, TypeError): pass
        try: self.num_followers = self.json['user']['numFollowers']
        except(KeyError, TypeError): pass
        try: self.num_following = self.json['user']['numFollowing']
        except(KeyError, TypeError): pass
        try: self.id = self.json['user']['id']
        except(KeyError, TypeError): pass
        try: self.socials = self.json['user']['socials']
        except(KeyError, TypeError): pass
        try: self.subscription = self.json['user']['subscription']
        except(KeyError, TypeError): pass
        try: self.subscription_id = self.json['user']['subscription']['id']
        except(KeyError, TypeError): pass
        try: self.subscription_plan = self.json['user']['subscription']['plan']
        except(KeyError, TypeError): pass
        try: self.subscription_plan_provider = self.json['user']['subscription']['plan']['provider']
        except(KeyError, TypeError): pass
        try: self.subscription_plan_cycle = self.json['user']['subscription']['plan']['cycle']
        except(KeyError, TypeError): pass
        try: self.subscription_plan_ends_at = self.json['user']['subscription']['plan']['ends_at']
        except(KeyError, TypeError): pass
        try: self.subscription_plan_started_at = self.json['user']['subscription']['plan']['started_at']
        except(KeyError, TypeError): pass
        try: self.subscription_plan_will_renew = self.json['user']['subscription']['plan']['will_renew']
        except(KeyError, TypeError): pass
        try: self.subscription_product = self.json['user']['subscription']['product']
        except(KeyError, TypeError): pass
        try: self.subscription_product_order = self.json['user']['subscription']['product']['order']
        except(KeyError, TypeError): pass
        try: self.subscription_product_name = self.json['user']['subscription']['product']['name']
        except(KeyError, TypeError): pass
        try: self.subscription_product_display_name = self.json['user']['subscription']['product']['display_name']
        except(KeyError, TypeError): pass
        try: self.subscription_product_display_name_without_emoji = self.json['user']['subscription']['product']['display_name_without_emoji']
        except(KeyError, TypeError): pass
        try: self.subscription_product_price = self.json['user']['subscription']['product']['price']
        except(KeyError, TypeError): pass
        try: self.subscription_product_price_monthly = self.json['user']['subscription']['product']['price']['monthly']
        except(KeyError, TypeError): pass
        try: self.subscription_product_price_Yearly = self.json['user']['subscription']['product']['price']['yearly']
        except(KeyError, TypeError): pass
        try: self.subscription_product_creditsPerMonth = self.json['user']['subscription']['product']['creditsPerMonth']
        except(KeyError, TypeError): pass
        try: self.subscription_product_stripe = self.json['user']['subscription']['product']['stripe']
        except(KeyError, TypeError): pass
        try: self.subscription_product_stripe_yearly = self.json['user']['subscription']['product']['stripe']['yearly']
        except(KeyError, TypeError): pass
        try: self.subscription_product_stripe_monthly = self.json['user']['subscription']['product']['stripe']['monthly']
        except(KeyError, TypeError): pass
        try: self.subscription_product_paypal = self.json['user']['subscription']['product']['paypal']
        except(KeyError, TypeError): pass
        try: self.subscription_product_paypal_yearly = self.json['user']['subscription']['product']['paypal']['yearly']
        except(KeyError, TypeError): pass
        try: self.subscription_product_paypal_monthly = self.json['user']['subscription']['product']['paypal']['monthly']
        except(KeyError, TypeError): pass
        try: self.subscription_product_color = self.json['user']['subscription']['product']['color']
        except(KeyError, TypeError): pass
        try: self.subscription_product_colorClasses = self.json['user']['subscription']['product']['colorClasses']
        except(KeyError, TypeError): pass
        try: self.subscription_product_colorClasses_text = self.json['user']['subscription']['product']['colorClasses']['text']
        except(KeyError, TypeError): pass
        try: self.subscription_product_colorClasses_background = self.json['user']['subscription']['product']['colorClasses']['background']
        except(KeyError, TypeError): pass
        try: self.favorite_images = self.json['user']['favoriteImages']
        except(KeyError, TypeError): pass
        for _ in self.favorite_images:
            try: self.favorite_images_id.append(_['id'])
            except(KeyError, TypeError): pass
            try: self.favorite_image_keys.append(_['key'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_private.append(_['private'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_model.append(_['model'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_creation_type.append(_['creation_type'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_creator.append(_['creator'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_created_at.append(_['created_at'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_rand_id.append(_['rand_id'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_likes.append(_['likes'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_prompt.append(_['prompt'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_prompt.append(_['nsfw'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_prompt_ts.append(_['prompt_ts'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_metadata.append(_['metadata'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_creator_name.append(_['creator_name'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_created_at.append(_['created_at'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_model_display_name.append(_['model_display_name'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_model_name.append(_['model_name'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_liked.append(_['liked'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_downloaded.append(_['downloaded'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_tagged.append(_['tagged'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_size.append(_['size'])
            except(KeyError, TypeError): pass
            try: self.favorite_images_favorited.append(_['favorited'])
            except(KeyError, TypeError): pass
        return self

class obj_get_image_children:
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
    def obj_get_image_children(self):
        for _ in self.json:
            try: self.key.append(_['key'])
            except(KeyError, TypeError): pass
            try: self.likes.append(_['likes'])
            except(KeyError, TypeError): pass
            try: self.private.append(_['private'])
            except(KeyError, TypeError): pass
            try: self.prompt.append(_['prompt'])
            except(KeyError, TypeError): pass
            try: self.creator.append(_['creator'])
            except(KeyError, TypeError): pass
            try: self.image_created_at.append(_['image_created_at'])
            except(KeyError, TypeError): pass
            try: self.creator_name.append(_['creator_name'])
            except(KeyError, TypeError): pass
            try: self.liked.append(_['liked'])
            except(KeyError, TypeError): pass
            try: self.downloaded.append(_['downloaded'])
            except(KeyError, TypeError): pass
            try: self.tagged.append(_['tagged'])
            except(KeyError, TypeError): pass
            try: self.has_thumbnail.append(_['has_thumbnail'])
            except(KeyError, TypeError): pass
            try: self.time_string.append(_['has_thumbnail'])
            except(KeyError, TypeError): pass
            try: self.model_name.append(_['model_name'])
            except(KeyError, TypeError): pass
            try: self.size.append(_['size'])
            except(KeyError, TypeError): pass
        return self

