# 🎬 MP4 + SRT Merger / Birleştirici

This Python script automatically merges `.mp4` video files with matching `.srt` subtitle files into `.mkv` format using `mkvmerge`, then deletes the original files.  
Bu Python betiği, aynı adı taşıyan `.mp4` ve `.srt` dosyalarını `mkvmerge` kullanarak `.mkv` formatında birleştirir ve ardından orijinal dosyaları siler.

## ✅ Features / Özellikler
- 🔍 Scans directories and subdirectories for `.mp4` and `.srt` files  
- 🎯 Matches files by name (e.g., `video.mp4` ↔ `video.srt`)  
- 🎞 Creates `.mkv` outputs via `mkvmerge`  
- 🧹 Deletes the original `.mp4` and `.srt` files after merging  
- 💻 No external Python packages required  

## 🛠 Requirements / Gereksinimler
- Python 3.6 or newer  
- [MKVToolNix](https://mkvtoolnix.download/) — `mkvmerge` must be in system PATH

Check if `mkvmerge` is installed:
```bash
mkvmerge --version
```

## 📦 Installation / Kurulum
```bash
git clone https://github.com/omruzn/mp4-srt-merger.git
cd mp4-srt-merger
```

Edit the script and set your directory path:
```python
root_folder = 'E:\\birlestir'
```

## ▶️ Usage / Kullanım
Run the script:
```bash
python mp4-srt-merger.py
```

Script şunları yapar:
1. Aynı ada sahip `.mp4` ve `.srt` dosyalarını bulur  
2. Bunları `.mkv` formatında birleştirir  
3. Orijinal dosyaları siler  

## 🗂 Example Folder Structure / Örnek Klasör Yapısı

**Before:**
```
E:\birlestir
├── movie1.mp4
├── movie1.srt
├── movie2.mp4
├── movie2.srt
```

**After:**
```
E:\birlestir
├── movie1.mkv
├── movie2.mkv
```

## ⚠️ Notes / Notlar
- ❗ The script **permanently deletes** the original `.mp4` and `.srt` files.  
- ✅ Only files with **matching names** are merged.  
- 🧪 `mkvmerge` must be installed and accessible from command line.

Created with ❤️ by [Ömer Uzun](https://github.com/omruzn)
