from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd
from tqdm import tqdm

downloader = YoutubeCommentDownloader()

video_url = "______________________yt_video_link____________________" 

comments = []
TARGET = 50000

for comment in tqdm(downloader.get_comments_from_url(video_url)):
    comments.append(comment['text'])
    if len(comments) >= TARGET:
        break

df = pd.DataFrame(comments, columns=["Comment"])
df.to_csv("youtube_ai_comments.csv", index=False)

print("Scraping completed ✅ Rows:", len(df))
