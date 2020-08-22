# pip install urllib
# pip install m3u8
# pip install streamlink
# -*- coding: utf-8 -*-
import urllib
import m3u8 #video file generator
import streamlink #Streamlink is a CLI utility which pipes video streams from various services into a video player, such as VLC.


def get_stream(url):
    """
    Get upload chunk url
    """
    streams = streamlink.streams(url)
    stream_url = streams["best"]

    m3u8_obj = m3u8.load(stream_url.args['url'])
    return m3u8_obj.segments[0]


def dl_stream(url, filename, chunks):
    """
    Download each chunks
    """
    pre_time_stamp = 0
    for i in range(chunks+1):
        stream_segment = get_stream(url)
        cur_time_stamp = \
            stream_segment.program_date_time.strftime("%Y%m%d-%H%M%S")

        if pre_time_stamp == cur_time_stamp:
            pass
        else:
            print(cur_time_stamp)
            file = open(filename + '_' + str(cur_time_stamp) + '.ts', 'ab+')
            with urllib.request.urlopen(stream_segment.uri) as response:
                html = response.read()
                file.write(html)
            pre_time_stamp = cur_time_stamp


url = "https://www.youtube.com/watch?v=AFNUeUed8Ro" #sky news live channel from youtube



# url=url.encode('utf-8').decode()
dl_stream(url, "live", 10) # will capture the live video frames, approx 5 seconds of live stream will be captured in each file