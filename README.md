This project is for educational and personal use only.
Users must comply with YouTube, TikTok, and copyright laws.
Do not download videos that you do not have permission to download.

# Video Downloader

This project lets you download videos from YouTube and TikTok using Python and yt-dlp.

## Features

- Download YouTube videos
- Download TikTok videos
- Choose the platform from a menu in the script
- Save files as MP4 when possible

## Requirements

- Python 3
- Node.js
- FFmpeg
- curl_cffi (for TikTok support)
- Windows PowerShell

## Step 1: Open PowerShell

Open PowerShell in the project folder.

## Step 2: Go to the project folder

```powershell
cd "your-project-folder"
```

## Step 3: Install the required packages

```powershell
.\.venv\Scripts\python.exe -m pip install yt-dlp curl_cffi
```

## Step 4: Install FFmpeg

Download FFmpeg and install it on Windows.

Recommended folder:

```powershell
C:\ffmpeg\bin
```

Add it to PATH:

```powershell
$ffmpegFolder = "C:\ffmpeg\bin"
[Environment]::SetEnvironmentVariable(
  "Path",
  [Environment]::GetEnvironmentVariable("Path", "User") + ";$ffmpegFolder",
  "User"
)
```

Close PowerShell and open a new window after that.

## Step 5: Verify FFmpeg works

```powershell
ffmpeg -version
```

If the command shows version details, FFmpeg is installed correctly.

## Step 6: Run the script

```powershell
cd "your-project-folder"
python download_manager.py
```

## Step 7: Choose a platform

When the script starts, it will ask:

```text
Choose a platform:
1. YouTube
2. TikTok
```

Enter:

- 1 for YouTube
- 2 for TikTok

Then paste the video URL.

## Example usage

### YouTube

```text
Enter 1 or 2: 1
Enter the URL: https://www.youtube.com/watch?v=VIDEO_ID_EXAMPLE
```

### TikTok

```text
Enter 1 or 2: 2
Enter the URL: https://www.tiktok.com/@exampleuser/video/1234567890123456789
```

## Troubleshooting

### Error: ffmpeg is not installed

Install FFmpeg and add its folder to PATH.

### Error: No module named yt_dlp

Run:

```powershell
.\.venv\Scripts\python.exe -m pip install yt-dlp
```

### Error: TikTok impersonation is not available

Run:

```powershell
.\.venv\Scripts\python.exe -m pip install curl_cffi
```

Then run the script again.

### Error: Requested format is not available

Make sure:

- yt-dlp is updated
- Node.js is installed
- FFmpeg is installed and available in PATH
- the video is public and supported by the site

## Notes

- YouTube downloads usually work best with FFmpeg installed.
- TikTok downloads can be less reliable because the site blocks some requests.
- Some videos may still fail because of platform protection or copyright restrictions.

## Final command to run

```powershell
cd "your-project-folder"
python download_manager.py
```
#
