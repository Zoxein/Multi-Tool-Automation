import os
import shutil

class FileManager:
    @staticmethod
    def organize_folder():
        print("\n" + "-"*20)
        print("   FILE ORGANIZER TARGET   ")
        print("-"*20)
        
        target_dir = input("Enter the full path of the folder to organize (e.g., C:\\Users\\Name\\Downloads): ").strip()
        
        if not os.path.exists(target_dir):
            print("[-] Custom path does not exist! Check it again, Bro.")
            return

        file_types = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
            "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Programs": [".exe", ".msi"],
            "Videos": [".mp4", ".mkv", ".avi", ".mov"]
        }

        print("[ * ] Organizing files... Please wait.")
        
        moved_count = 0 

        try:
            for filename in os.listdir(target_dir):
                file_path = os.path.join(target_dir, filename)
                
                if os.path.isfile(file_path):
                    _, file_ext = os.path.splitext(filename)
                    file_ext = file_ext.lower()
                    
                    moved = False
                    for folder_name, extensions in file_types.items():
                        if file_ext in extensions:
                            destination_folder = os.path.join(target_dir, folder_name)
                            if not os.path.exists(destination_folder):
                                os.makedirs(destination_folder)
                            
                            shutil.move(file_path, os.path.join(destination_folder, filename))
                            moved_count += 1
                            moved = True
                            break
                    
                    if not moved:
                        others_folder = os.path.join(target_dir, "Others")
                        if not os.path.exists(others_folder):
                            os.makedirs(others_folder)
                        shutil.move(file_path, os.path.join(others_folder, filename))
                        moved_count += 1

            print(f"[+] Done! Successfully organized {moved_count} files. 🔥")

        except Exception as e:
            print(f"[-] An error occurred during organizing: {e}")