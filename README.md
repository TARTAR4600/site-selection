# site-selection
整个前

V：目前用油管测试，下载和转音频没有问题，第四步死

## 1.在download_list.txt中存放视频url

## 2.下载内容（scr路径下）

```bash
yt-dlp --batch-file download_list.txt \  --output "videos/%(uploader)s_%(upload_date)s_%(id)s.%(ext)s"
```

## 3.将视频分离出音频

```bash
python videos-audios.py 
```

## 4.转文字（api额度不够哈哈）
跑 `apiTransToWords.py`