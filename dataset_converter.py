import os
import shutil

src_root = 'tongue'                  # 資料來源目錄
dst_img_dir = os.path.join(src_root, 'images')
dst_ann_dir = os.path.join(src_root, 'annots')

os.makedirs(dst_img_dir, exist_ok=True)
os.makedirs(dst_ann_dir, exist_ok=True)

for folder in os.listdir(src_root):
    subdir = os.path.join(src_root, folder)
    if os.path.isdir(subdir):
        img_src = os.path.join(subdir, 'img.png')
        label_src = os.path.join(subdir, 'label.png')
        # 新檔名為「資料夾名稱_img.png」與「資料夾名稱_label.png」
        img_dst = os.path.join(dst_img_dir, f'{folder}.png')
        label_dst = os.path.join(dst_ann_dir, f'{folder}.png')
        if os.path.exists(img_src) and os.path.exists(label_src):
            shutil.copy(img_src, img_dst)
            shutil.copy(label_src, label_dst)
            print(f'Copied {img_src} -> {img_dst}')
            print(f'Copied {label_src} -> {label_dst}')
        else:
            print(f'[WARNING] Skipped {folder} (img.png or label.png not found)')
