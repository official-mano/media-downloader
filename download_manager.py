import shutil

import yt_dlp

try:
    from yt_dlp.networking.impersonate import ImpersonateTarget
except Exception:  # pragma: no cover
    ImpersonateTarget = None


def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        raise SystemExit(
            "FFmpeg is required to merge video and audio into one file. "
            "Install FFmpeg and add it to PATH, then run the script again."
        )


def download_youtube(url: str):
    check_ffmpeg()

    ydl_opts = {
        "format": "bv*+ba/b",
        "js_runtimes": {"node": {}},
        "noplaylist": True,
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_tiktok(url: str):
    impersonate_target = (
        ImpersonateTarget.from_str("chrome") if ImpersonateTarget else "chrome"
    )

    ydl_opts = {
        "format": "best",
        "noplaylist": True,
        "outtmpl": "%(title)s.%(ext)s",
        "impersonate": impersonate_target,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.YoutubeDLError as exc:
        if "Impersonate target" in str(exc) or "impersonate" in str(exc).lower():
            raise SystemExit(
                "TikTok impersonation is not available. Install the required dependency with:\n"
                "\.\\.venv\\Scripts\\python.exe -m pip install curl_cffi\n"
                "Then run the script again."
            ) from exc
        raise


if __name__ == "__main__":
    print("Choose a platform:")
    print("1. YouTube")
    print("2. TikTok")

    choice = input("Enter 1 or 2: ").strip()

    url = input("Enter the URL: ").strip()

    if not url:
        print("No URL entered.")
        raise SystemExit

    if choice == "1":
        download_youtube(url)
    elif choice == "2":
        download_tiktok(url)
    else:
        print("Invalid choice. Please enter 1 or 2.")
