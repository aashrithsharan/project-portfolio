# MP4 to MP3 Converter

A simple Python GUI application to convert MP4 video files to MP3 audio format, supporting all codecs.

## Features

- 🎵 Convert MP4 videos to MP3 audio
- 📁 Batch conversion support (multiple files at once)
- 🎨 Simple and intuitive GUI interface
- 🔄 Progress tracking for conversions
- ✅ Support for all video codecs (via FFmpeg)
- 💪 High-quality audio output

## Requirements

- Python 3.7 or higher
- FFmpeg (must be installed and in system PATH)

## Installation

### 1. Install Python
Download and install Python from python.org

### 2. Install FFmpeg

#### Windows:
1. Download FFmpeg from ffmpeg.org
2. Extract the archive
3. Add the `bin` folder to your system PATH
4. Verify installation: Open Command Prompt and run `ffmpeg -version`

#### macOS:
```bash
brew install ffmpeg
```

#### Linux:
```bash
sudo apt update
sudo apt install ffmpeg
```

### 3. Clone or Download This Project
```bash
cd "c:\MP4 to MP3"
```

## Usage

### Run the Application
```bash
python mp4_to_mp3_converter.py
```

### Steps to Convert:
1. Click **"Select MP4 Files"** to choose one or more MP4 files
2. Click **"Select Output Folder"** to choose where to save the MP3 files
3. Click **"Convert to MP3"** to start the conversion
4. Wait for the process to complete

## Technical Details

### Audio Quality
- Uses `libmp3lame` codec for MP3 encoding
- Quality setting: `-q:a 2` (high quality, scale 0-9 where lower is better)
- Variable bitrate (VBR) for optimal file size and quality

### FFmpeg Command
```bash
ffmpeg -i input.mp4 -vn -acodec libmp3lame -q:a 2 output.mp3
```

## Troubleshooting

### FFmpeg Not Found
If you get an error about FFmpeg not being found:
1. Make sure FFmpeg is installed
2. Verify it's in your system PATH by running `ffmpeg -version` in terminal
3. Restart the application after installing FFmpeg

### Conversion Fails
- Check that the input file is a valid MP4 file
- Ensure you have write permissions to the output folder
- Verify the MP4 file contains audio (some videos are video-only)

## License

This project is for personal use. FFmpeg is licensed under LGPL/GPL.

## Credits

Built with:
- Python Tkinter (GUI)
- FFmpeg (conversion engine)
