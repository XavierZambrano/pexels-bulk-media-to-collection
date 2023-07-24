Add pexels media in bulk to pexels collection


### Usage

The simplest script:
```
from api import API


pexels_session = 'xxxxxxxxxxxxxxxxxxxx'
collection_id = 'xxxxxxxx'
media_url = 'https://www.pexels.com/photo/america-architecture-bay-boat-208745/'

api = API(pexels_session)
api.add_media_to_collection(media_url, collection_id)

```

You can combine with another libs and get all the media_url of a collection, or a search query. For example, with [pexels-api](https://github.com/AguilarLagunasArturo/pexels-api) (I have a fork that support collections [pexels-api](https://github.com/XavierZambrano/pexels-api)) or [pypexels](https://github.com/salvoventura/pypexels) 