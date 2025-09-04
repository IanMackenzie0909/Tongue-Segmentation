_base_ = [
    './config/tongue_custom.py',
    '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]

norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    type='EncoderDecoder',
    pretrained=None,
    backbone=dict(
        type='UNet',
        in_channels=3,
        base_channels=64,
        num_stages=5,
        strides=(1, 1, 1, 1, 1),
        enc_num_convs=(2, 2, 2, 2, 2),
        dec_num_convs=(2, 2, 2, 2),
        downsamples=(True, True, True, True),
        enc_dilations=(1, 1, 1, 1, 1),
        dec_dilations=(1, 1, 1, 1),
        norm_cfg=norm_cfg,
        act_cfg=dict(type='ReLU'),
        upsample_cfg=dict(type='InterpConv'),
        norm_eval=False,
        style='pytorch'),
    decode_head=dict(
        type='UNetHead',
        in_channels=64,
        channels=64,
        num_classes=2,          # 兩個類別
        norm_cfg=norm_cfg,
        concat_input=True,
        dropout_ratio=0.1,
        upsample_cfg=dict(type='InterpConv'),
        align_corners=False,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0)),
    auxiliary_head=dict(
        type='FCNHead',
        in_channels=64,
        channels=32,
        num_convs=1,
        num_classes=2,         # 兩個類別
        norm_cfg=norm_cfg,
        concat_input=False,
        dropout_ratio=0.1,
        align_corners=False,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
    # model training/testing settings
    train_cfg=dict(),
    test_cfg=dict(mode='whole')
)
