# ExtractVideoMetadata

# OverView

This is API which is implemented by Flask. We send video as a post request to this API. API returns metadata and the number of people. number of people is detected by a pre-trained model and OpenCV based on every frame of uploaded the video. Every response is going to store into the database as a log.


# Usage

1. Git Clone: ```https://github.com/atsushii/ExtractVideoMetadata.git```

2. Build docker image and run container: ```docker-compose up --build -d```

3. Into container (We need to migrate database): ```docker-compose exec web bash```

4. Initialize db: ``` flask db init```

5. Migrate: ```flask db migrate```

6. Upgrade: ``` flask db upgrade```

7. Finally Use postman to send a post request to API

  **Success Response**
  ```
  {
  "count_person": {
      time (ms): counted number of the people
  },
  "metadata": [
    {
      "create_time": value,
      "duration": value,
      "filename": value,
      "height": value,
      "mime_type": value,
      "width": value
    }
  ],
  "status": "ok"
}
```
  **Error Response**

  ```{"status": False, "metadata": ""} ```

# unittest coverage
```
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
app/__init__.py                          26      7    73%
app/config.py                            16      0   100%
app/models/models.py                      9      1    89%
app/tests/test_endpoint.py               38      1    97%
app/tests/test_extract_meta_data.py      57      0   100%
app/tests/test_handle_video_file.py      29      0   100%
app/utils/execute_log_table.py            7      0   100%
app/utils/extract_meta.py                32      0   100%
app/utils/handle_video_file.py           19      1    95%
app/utils/yolo_video.py                  55      0   100%
app/views/views.py                       23      0   100%
---------------------------------------------------------
TOTAL                                   311     10    97%
```

# What did I implement

・ writtenin Python

・ A single endpoint

・ Endpoint accepts a video via the body of a POST request

・ Endpoint returns JSON-formatted information about the input video

・ The API is packaged in a docker image

・ Use additional docker image/container to serve a database with a single log table. Table stores the timestamps and return data for any API requests

・ Unit testing for endpoint and any other classes/functions implemented

・ Application of a pre-trained model to extract the information returned from the video

# Stack

/ Python
/ Flask
/ Docker
/ unittest
/ CNN
/ MySQL





