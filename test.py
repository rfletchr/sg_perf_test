import os
import time
import tempfile
import shotgun_api3

version_id = 74131

sg = shotgun_api3.Shotgun(
    base_url="https://wlvfx.shotgrid.autodesk.com",
    script_name="pipetest2",
    api_key="pno9zijmnist~qzeehfhldbWs",
)

version = sg.find_one("Version", [["id","is",version_id]], ["sg_uploaded_movie"])

start_download = time.time()
file_path = tempfile.mktemp(suffix=".mov")

download_url = sg.get_attachment_download_url(version["sg_uploaded_movie"])
print(download_url)

sg.download_attachment(attachment=version["sg_uploaded_movie"], file_path=file_path)

#format the time using strftime
end_download = time.time()
time_str = time.strftime("%H:%M:%S", time.gmtime(end_download - start_download))

file_size = os.path.getsize(file_path)
mb_size = round(file_size / 1024 / 1024)
print("Downloaded file to %s (%s MB) in %s" % (file_path, mb_size, time_str))


start_upload = time.time()
sg.upload("Version", version_id, file_path, field_name="sg_uploaded_movie")
end_upload = time.time()
time_str = time.strftime("%H:%M:%S", time.gmtime(end_upload - start_upload))
print("Uploaded file from %s in %s" % (file_path, time_str))





