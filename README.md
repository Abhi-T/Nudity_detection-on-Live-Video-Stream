# Nudity_detection-on-Live-Video-Stream
Nudity_detection-on-Live-Video-Stream



readVideoStream.py--> Extract video content from online platform, duration can be controlled. Example 5 seconds of video frame can be extracted from live platform

producer.py-->  reads the video file frame by frame and publish to KAFKA topic in byte format

consumer.py--> consumes KAFKA messages and convert byte to image format for prediction

predict.py-->  nudity detection model
