dataset_type = 'CustomDataset'
data_root = 'tongue/'

classes = ('_background_', 'tongue')  # 根據你的 label_names.txt
palette = [
    [0, 0, 0],      # _background_ (黑色)
    [255, 0, 0],    # tongue (紅色，可自訂)
]

img_suffix = '.png'
seg_map_suffix = '.png'

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='Resize', img_scale=(400, 400), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PackSegInputs')
]

train_dataloader = dict(
    batch_size=4,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='images',
        ann_dir='annots',
        pipeline=train_pipeline,
        classes=classes,
        palette=palette
    )
)
val_dataloader = train_dataloader.copy()
test_dataloader = train_dataloader.copy()
