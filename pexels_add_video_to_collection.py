import requests
from pexels_api import API
from pexels_api.tools.utils import filter_video_entries
from api import API as PexelsCollectionAPI
from api import get_media_id
import json


query = 'seascapes'

collections = {
    'ulshmms': 'clouds',
    'tnlcvid': 'aesthetic',
    'ukf5eew': 'seascapes',
    'n9ohu1g': 'abstract',
    'cchtbkb': 'water',
    '4mytdvq': 'animals',
    'ddj9qge': 'cute animals',
    'njz3pe6': 'scenic',
    'dp70axj': 'buildings',
    'rbrpbzs': 'timelapse',
    'nhhpsof': 'marine life',
    'jszvnup': 'window rain',
    'ctrioxj': 'book open',
    'lg0xcid': 'beautiful background',
    'a99t1kl': 'autumn forest',
    'zggdekd': 'sunsets',
    'rgzwev5': 'night',
}
# get the collection id using query and collections
collection_id = None
for collection in collections:
    if collections[collection] == query:
        collection_id = collection
        break
if collection_id:
    print(f'Collection id: {collection_id}')
else:
    print('Collection not found')
    quit()
last_queries = ['clouds']
# passed
# clouds, aesthetic

PEXELS_API_KEY = 'L8kU0HI4vo9cHELeTLxQPpGR9c2z3O7Ruy28QVfhQBmEqvpAJARwkTpz'
PEXELS_SESSION = 'pL%2F9SE0yz6lASJiH2RiqHi9xVyINVO0yNouNjwlUA9Cb3%2B5vi6yXlRubbZXP3gpFpAzK398TR8d%2B8ROSLPLF7HdISTYOGZ2%2FICs2UzzXCkZhOUNDvG0QcmsAcNzCxnZePwcEsaJIpcwzxvIKTxR7z9R7h68p%2BYzWs9JcPNLdwLMezl%2BvJ6DoDrvoMYN4Ow4nVwDQixXM0wiVm94xIKqt0pjpATz6HpRuR8CV8Fffszpt5DEZII4yVOWKhZlxOwBvkIL656vOuXz%2FzcOu9r7CDInY6x9PHDaukQKldcceT1ODgYOfDEG8MdZxYPvITzjlbYhN4X7dl0hdvhKFJcPq1YnnIDpI%2BoutCxChLDd2kbaPimMy1LFqpoYOfI7JuoListFqRxZW9SjBimw%3D--dkKcKVaGMZS2u9Q6--LgTan%2F6wodZ91DsJQNOdaA%3D%3D'
api_collections_bulk = PexelsCollectionAPI(PEXELS_SESSION)

if query in last_queries:
    print('Already added')
    quit()

api = API(PEXELS_API_KEY)
api.search_video(query=query, page=1, results_per_page=1, orientation='portrait', size='medium')
print(f'Total results: {api.total_results}')

with open('collections_bulk.json', 'r', encoding='utf-8') as f:
    content = json.load(f)
if collection_id in content.keys():
    pass
else:
    content[collection_id] = []
    with open('collections_bulk.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)
quit()
i = 0
for page in range(1, 10):
    print('Page:', page)
    api.search_video(query, page=page, results_per_page=50, orientation='portrait', size='medium')
    videos = api.get_video_entries()
    print(len(videos))
    if videos:
        pass
    else:
        print('No more videos')
        break

    videos = filter_video_entries(videos, min_duration=20, orientation='portrait', min_size='medium')
    for video in videos:
        # This is for when i delete videos manually because I don't like don't add it to the collection again
        with open('collections_bulk.json', 'r', encoding='utf-8') as f:
            content = json.load(f)

        media_id = get_media_id(video.url)
        if media_id in content[collection_id]:
            print(f'{media_id}, added before')
            continue
        try:
            print(f'collection_id {collection_id}')
            media_id = api_collections_bulk.add_media_to_collection(video.url, collection_id)
            content[collection_id].append(media_id)
            with open('collections_bulk.json', 'w', encoding='utf-8') as f:
                json.dump(content, f, ensure_ascii=False, indent=4)

            i += 1
        except ValueError as e:
            print(e)


print('Total videos added:', i)
