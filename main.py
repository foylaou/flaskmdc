from flask import Flask, render_template, send_from_directory, abort
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

path = "fileshare"


@app.route('/')
def list_files():
    directory = os.path.join(app.root_path, path)
    files = os.listdir(directory)
    # 使用 render_template 顯示檔案列表
    return render_template('files_list.html', files=files)


@app.route('/files/<path:filename>')
def download_file(filename):
    directory = os.path.join(app.root_path, path)
    try:
        return send_from_directory(directory, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
