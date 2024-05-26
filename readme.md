<h2 align = "center">artbreeder</h2>
<details>
<summary>reveal me : </summary>

###### This library is intended for requests to the artbreeder website
###### Эта библиотека предназначена для запросов на сайт artbreeder
###### example/Пример :

```py3
from artbreeder import Artbreeder

Artbreeder.login(email = 'email', password = 'password')

for _ in Artbreeder.get_posts():
    Artbreeder.add_comment(
        text = 'Is cool!',
        post_key = _.key
    )
    
Artbreeder.new_username(old_username = 'Proxy1Mallet', 
                        new_username = 'Proxy1Mistake',
                        email = 'email')

Artbreeder.new_mail(email = 'new_email')

Artbreeder.logout()
```
</details>

<details>
<summary>ᴍʏ sᴏᴄɪᴀʟ ɴᴇᴛᴏᴡʀᴋ : </summary>
<br>
<a href = "https://t.me/Proxy1Mistake" target="_blank">
<img src = "https://img.shields.io/badge/ᴛᴇʟᴇɢʀᴀᴍ-92000a?logo=telegram&logoColor=FFFFFF&labelColor=000000">
<a href = "https://discordapp.com/users/875370793100533862/" target="_blank">
<img src = "https://img.shields.io/badge/ᴅɪsᴄᴏʀᴅ-92000a?logo=discord&logoColor=FFFFFF&labelColor=000000">
</br>
</details>
</h4>
