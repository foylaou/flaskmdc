from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import tempfile
import shutil

app = Flask(__name__)

# 設置暫存檔案夾用於保存上傳的檔
UPLOAD_FOLDER = tempfile.mkdtemp()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# 處理上傳的文字檔
def process_text(file_path):
    start_text = "<key>allowActivityContinuation</key>"
    end_text = "<key>forceWiFiWhitelisting</key>"
    with open('rep1', 'r+', encoding='utf-8') as f:
        replacement_text = f.read()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        # 查找起始点和终点之间的文本
        start_index = content.find(start_text)
        end_index = content.find(end_text) + len(end_text)

        if start_index != -1 and end_index != -1:
            # 找到起始点和终点，进行替换
            modified_content = content[:start_index] + replacement_text + content[end_index:]
            return modified_content


    except UnicodeDecodeError:
        return "無法解碼檔，請確保檔使用正確的編碼。"


def process_text2(file_path):
    start_text = "<key>allowActivityContinuation</key>"
    end_text = "<key>forceWiFiWhitelisting</key>"
    with open('rep2', 'r+', encoding='utf-8') as f:
        replacement_text = f.read()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        # 查找起始点和终点之间的文本
        start_index = content.find(start_text)
        end_index = content.find(end_text) + len(end_text)

        if start_index != -1 and end_index != -1:
            # 找到起始点和终点，进行替换
            modified_content = content[:start_index] + replacement_text + content[end_index:]
            return modified_content


    except UnicodeDecodeError:
        return "無法解碼檔，請確保檔使用正確的編碼。"


# 主頁，用於上傳文件
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 獲取上傳的文件
        uploaded_file = request.files['file']

        if uploaded_file:
            # 保存上傳的檔到暫存檔案夾
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(file_path)

            # 處理文字檔
            processed_text = process_text(file_path)
            processed_text2 = process_text2(file_path)
            return render_template('result.html', text=processed_text, text2=processed_text2)

    return render_template('index.html')


# 處理方式1：下載處理後的文字檔
@app.route('/download')
def download():
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'btunlock.mobileconfig')

    # 將處理後的文本保存到新的檔
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(request.args.get('text', ''))

    # 提供下載連結
    return send_file(file_path, as_attachment=True)


# 處理方式2：在網頁上顯示處理結果
@app.route('/download2')
def download2():
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'unlock.mobileconfig')

    # 將處理後的文本保存到新的檔
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(request.args.get('text', ''))

    # 提供下載連結
    return send_file(file_path, as_attachment=True)


# 處理方式3：發送處理結果到使用者的電子郵件（未實現）
@app.route('/email')
def email():
    # 在此處添加發送電子郵件的代碼
    # 可以使用Python的smtplib庫來發送電子郵件
    return "處理結果已發送到您的電子郵件。"


if __name__ == '__main__':
    app.run(debug=True)
