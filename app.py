from flask import Flask, render_template, request, jsonify
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    video_urls = data.get('videoUrls')
    try:
        download_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Jaydeep')
        os.makedirs(download_path, exist_ok=True)
        
        for video_url in video_urls:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            
            video_filename = f'{yt.title}.mp4'
            video_filepath = os.path.join(download_path, video_filename)

            # Download the video
            stream.download(download_path)

        return jsonify({'success': True, 'message': "Thanks for choosing Jaydeep Omprakash Sharma's YT Downloader. Your videos are in downloading progress. Have a great day!"})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
