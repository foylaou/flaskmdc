# 定义要替换的起始点和终点文本
start_text = "<key>allowActivityContinuation</key>"
end_text = "<key>forceWiFiWhitelisting</key>"
replacement_text = "test"

# 打开文件进行读取和写入
with open('bt.mobileconfig', 'r', encoding='utf-8') as file:
    content = file.read()

# 查找起始点和终点之间的文本
start_index = content.find(start_text)
end_index = content.find(end_text) + len(end_text)

if start_index != -1 and end_index != -1:
    # 找到起始点和终点，进行替换
    modified_content = content[:start_index] + replacement_text + content[end_index:]

    # 将修改后的内容写回文件
    with open('bt0.mobileconfig', 'w', encoding='utf-8') as output_file:
        output_file.write(modified_content)
else:
    # 如果未找到起始点或终点，不进行替换
    with open('bt0.mobileconfig', 'w', encoding='utf-8') as output_file:
        output_file.write(content)
