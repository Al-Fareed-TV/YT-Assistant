import yt_content_analyzer as yca

yt_url = input("Enter the YT url : ")
user_prommpt = input("Enter your query regarding to the YT video : ")

db = yca.create_db_from_youtube_video_url(yt_url)

response,docs = yca.get_response_from_query(db=db,query=user_prommpt)

print('\n',response)