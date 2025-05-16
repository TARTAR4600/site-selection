import openai
import os
from pathlib import Path

# 这个是我刚才新注册的api，有api git屏蔽我了
openai.api_key = ""

audio_folder = "../files/audios"
output_folder = "../files/transcripts"
os.makedirs(output_folder, exist_ok=True)

for file in Path(audio_folder).glob("*.wav"):
    print(f"🎧 正在转写: {file.name}")
    with open(file, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="verbose_json"
        )
    
    out_path = Path(output_folder) / f"{file.stem}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(transcript.model_dump_json(indent=2, ensure_ascii=False))
    
    print(f"✅ 已保存: {out_path.name}")

print("🚀 所有音频转写完成！")