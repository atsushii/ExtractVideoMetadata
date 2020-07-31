from flask import Flask, Blueprint, request, jsonify
from app.utils.extract_meta import ExtractMetaData
from app.utils.handle_video_file import HandleVideoFile
from app.utils.execute_log_table import ExecuteLogTable
from app.utils.yolo_video import YoloVideo

api = Blueprint("api", __name__)


@api.route("/fetch_video_information", methods=["POST"])
def fetch_video_information():

    if request.method == "POST":

        execute_log_table = ExecuteLogTable()

        video_data = request.files["data"]
        handle_video_file = HandleVideoFile("/api/uploads")
        cap, flag = handle_video_file.convert_to_videp_capture(video_data)

        # Check uploaded file is video
        if cap.isOpened() and flag:

            extract_meta_data = ExtractMetaData(video_data, cap)
            meta_data = extract_meta_data.create_meta_data()
            yolo_video = YoloVideo(cap)
            count_result = yolo_video.count_person()

            data = {"status": "ok", "metadata": meta_data,
                    "count_person": count_result}

            execute_log_table.store_log(data)

            return jsonify(data), 200

    data = {"status": False, "metadata": ""}
    execute_log_table.store_log(data)

    return jsonify(data), 400
