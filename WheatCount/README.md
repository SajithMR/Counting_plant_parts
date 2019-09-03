# Wheat Spike Counting
https://github.com/littleaich/heatmap-regulation adapted for wheat spike counting 


python main\_gap\_gas.py --train 1 --img-dir 'Traing image dir' --gam-dir 'Gam Image Dir' --ann-dir 'Annotaion file' --arch 'vgg16' --optim 'adam' --workers 8 --batch-size 8 --start-epoch 1 --end-epoch 100 --learning-rate 0.0001 --momentum 0.9 --weight-decay 0.0001 --save-interval 1 --print-freq 50

python main\_gap\_gas.py --train 0 --img-dir "/home/sajith/Data/cropped_wheat/halfed/test" --ann-dir "/home/sajith/Data/cropped_wheat/halfed/anno" --arch 'vgg16' --load-epoch 3

