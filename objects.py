from pydantic import BaseModel, Field, ConfigDict

class Comments(BaseModel):
    comment_id: int = Field(alias = 'comment_id')
    comment_parent_id: None | int = Field(alias = 'comment_parent_id')
    created_at: str = Field(alias = 'created_at')
    creator_profile_image_key: str = Field(alias = 'creatorProfileImageKey')
    creator_role: None | str = Field(alias = 'creatorRole')
    creator_username: str = Field(alias = 'creatorUsername')
    creator_id: int = Field(alias = 'creator_id')
    followed: bool = Field(alias = 'followed')
    has_blocked_current_user: bool = Field(alias = 'has_blocked_current_user')
    is_blocked_by_current_user: bool = Field(alias = 'is_blocked_by_current_user')
    key: str = Field(alias = 'key')
    liked: bool = Field(alias = 'liked')
    message: str = Field(alias = 'message')
    nsfw: bool = Field(alias = 'nsfw')
    num_comments: int = Field(alias = 'num_comments')
    num_likes: int = Field(alias = 'num_likes')
    num_reports: int = Field(alias = 'num_reports')
    post_id: int = Field(alias = 'post_id')
    violates_coc: bool = Field(alias = 'violates_coc')

    model_config = ConfigDict(protected_namespaces = ())

class Images(BaseModel):
    created_at: str = Field(alias = 'created_at')
    creation_type: int = Field(alias = 'creation_type')
    creator: int = Field(alias = 'creator')
    creator_id: int = Field(alias = 'creator_id')
    creator_name: str = Field(alias = 'creator_name')
    creator_profile_image_key: str = Field(alias = 'creator_profile_image_key')
    downloaded: bool = Field(alias = 'downloaded')
    id: int = Field(alias = 'id')
    image_created_at: str = Field(alias = 'image_created_at')
    is_current_contest_entry: None | bool = Field(alias = 'is_current_contest_entry')
    key: str = Field(alias = 'key')
    liked: bool = Field(alias = 'liked')
    likes: None | int = Field(alias = 'likes')
    model: int = Field(alias = 'model')
    model_name: str = Field(alias = 'model_name')
    nsfw: None | bool = Field(alias = 'nsfw')
    private: bool = Field(alias = 'private')
    prompt: None | str = Field(alias = 'prompt')
    prompt_ts: None | str = Field(alias = 'prompt_ts')
    rand_id: int = Field(alias = 'rand_id')
    size: list = Field(alias = 'size')
    tagged: bool = Field(alias = 'tagged')

    model_config = ConfigDict(protected_namespaces = ())

class GetPosts(BaseModel):
    comments: list[Comments] = Field(alias = 'comments')
    images: list[Images] = Field(alias = 'images')

    created_at: str = Field(alias = 'created_at')
    creation_date_sring: str = Field(alias = 'creationDateString')
    creator_id: int = Field(alias = 'creatorId')
    creator_profile_image_key: str = Field(alias = 'creatorProfileImageKey')
    creator_role: None | str = Field(alias = 'creatorRole')
    creator_username: str = Field(alias = 'creatorUsername')
    followed_by_current_user: bool = Field(alias = 'followedByCurrentUser')
    followed_by_current_user: bool = Field(alias = 'followedByCurrentUser')
    id: int = Field(alias = 'id')
    is_blocked_by_current_user: bool = Field(alias = 'isBlockedByCurrentUser')
    key: str = Field(alias = 'key')
    last_comment: str = Field(alias = 'last_comment')
    message: str = Field(alias = 'message')
    nsfw: bool = Field(alias = 'nsfw')
    num_comments: int = Field(alias = 'numComments')
    num_likes: int = Field(alias = 'numLikes')
    num_reports: int = Field(alias = 'numReports')
    num_views: int = Field(alias = 'numViews')
    rich_text: list = Field(alias = 'richText')
    this_user_has_liked: bool = Field(alias = 'thisUserHasLiked')
    type: int = Field(alias = 'type')
    username: str = Field(alias = 'username')
    violates_сoc: bool = Field(alias = 'violatesCoc')

    model_config = ConfigDict(protected_namespaces = ())