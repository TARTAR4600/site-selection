import os
import glob

# 输入输出路径
video_folder = "../files/videos"
audio_folder = "../files/audios"
os.makedirs(audio_folder, exist_ok=True)

# 遍历所有 .mp4 文件
for filepath in glob.glob(os.path.join(video_folder, "*.mp4")):
    filename = os.path.splitext(os.path.basename(filepath))[0]
    output_path = os.path.join(audio_folder, f"{filename}.wav")
    
    cmd = f'ffmpeg -i "{filepath}" -ar 16000 -ac 1 "{output_path}"'
    print(f"正在提取音频: {filename}")
    os.system(cmd)

print("✅ 音频提取完成！")
