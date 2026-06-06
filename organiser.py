from pathlib import Path
import shutil
import os
files = {"docs":['.docx','.xlsx','.txt','.pptx','.doc','.pdf','.csv'],
            "images":['.jpg','.jpeg','.png','.gif','.webp','.avif','.svg','.tiff','.tif'],
            "videos":['.mp4','.mov','.mkv','.avi','webm','.m4v'],
            "audios":['.mp3','.m4a','.aac','.ogg','.wav','.aiff','.aif','.flac','.alac'],
            "code":['.py','.js','.cpp','.cc','.java','.c'],
            "others":[]}
def file_cat(fext):
    for cat,ext in files.items():
        if fext in ext:
            return cat
    return "others"

def organise_files(path):
    folderpath=Path(path) #d:/organiserfolder/images
    skipped,moved=0,0
    if not folderpath.exists():
        print(f"Folder path is invalid. Check path: {folderpath}")
        return
    for file in folderpath.iterdir():
        if file.name.startswith(".") | file.is_dir():
            skipped=skipped+1
        else:
            category=file_cat(file.suffix)
            new_path=folderpath/category
            new_path.mkdir(exist_ok=True)
            shutil.move(str(file), str(new_path))
            moved=moved+1
            print(f"{file} moved to {new_path/file.name}")
    print(f"Total {moved} files moved...")       

if __name__ == "__main__":
    fpath = input("Type path of the folder in which files need to be organised")
    organise_files(fpath)

