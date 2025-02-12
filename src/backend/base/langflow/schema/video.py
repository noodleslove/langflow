import base64

import cv2


def is_video_file(file_path: str) -> bool:
    from langflow.base.data.utils import VIDEO_FILE_TYPES

    """Check if a file is a video file.

    Args:
        file_path: Path to the file.

    Returns:
        bool: True if the file is a video file, False otherwise.
    """
    return file_path.endswith(tuple(VIDEO_FILE_TYPES))


def get_video_frames(file_path: str, rate: int = 2) -> list[str]:
    """Get video frames from a video file.

    Args:
        file_path: Path to the video file.
        rate: Rate of the frames per second to be returned.

    Returns:
        A list of image URLs.
    """
    video = cv2.VideoCapture(file_path)
    step = max(1, int(video.get(cv2.CAP_PROP_FPS) / rate))
    frames = []
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        _, buffer = cv2.imencode(".jpg", frame)
        base64_image = base64.b64encode(buffer).decode("utf-8")
        image_url = f"data:image/jpeg;base64,{base64_image}"
        frames.append(image_url)

    video.release()
    return frames[::step]
