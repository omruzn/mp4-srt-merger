import os
import subprocess
import time

def find_files(root_folder):
    """
    Scans the given directory (and subdirectories) to find .mp4 and .srt files.
    Belirtilen klasördeki .mp4 ve .srt dosyalarını bulur.
    
    Returns:
        mp4_files (dict): Key = filename without extension, Value = full path to .mp4
        srt_files (dict): Key = filename without extension, Value = full path to .srt
    """
    mp4_files = {}
    srt_files = {}

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.mp4'):
                mp4_files[os.path.splitext(file)[0]] = os.path.join(root, file)
            elif file.endswith('.srt'):
                srt_files[os.path.splitext(file)[0]] = os.path.join(root, file)

    return mp4_files, srt_files

def delete_file(file_path):
    """
    Tries to delete the specified file and handles permission/file errors.
    Dosyayı silmeye çalışır, izin veya bulunamama hatalarını yönetir.
    """
    try:
        os.remove(file_path)
        print(f'Deleted: {file_path}')
    except PermissionError as e:
        print(f'Permission error: {e}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'Unknown error occurred: {e}')

def merge_files(mp4_files, srt_files):
    """
    Merges each .mp4 file with its corresponding .srt file into a .mkv file using mkvmerge.
    Eşleşen her .mp4 ve .srt dosyasını .mkv olarak birleştirir.
    """
    for name, mp4_path in mp4_files.items():
        srt_path = srt_files.get(name)
        if srt_path:
            output_mkv = mp4_path.replace('.mp4', '.mkv')
            command = ['mkvmerge', '-o', output_mkv, mp4_path, srt_path]
            try:
                subprocess.run(command, check=True)
                print(f'Merged: {mp4_path} + {srt_path} -> {output_mkv}')
                
                # Wait a short moment to ensure the OS releases file handles before deletion
                # Silme işleminden önce dosya kullanımının bitmesini bekler
                time.sleep(1)
                delete_file(mp4_path)
                delete_file(srt_path)

            except subprocess.CalledProcessError as e:
                print(f'Merge error: {e}')

if __name__ == '__main__':
    # Folder where .mp4 and .srt files are located
    # .mp4 ve .srt dosyalarının bulunduğu klasör
    root_folder = 'E:\\birlestir'
    mp4_files, srt_files = find_files(root_folder)
    merge_files(mp4_files, srt_files)
