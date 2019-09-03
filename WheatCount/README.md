# HR_Canola
https://github.com/littleaich/heatmap-regulation addapted for Canola flower counting 


python main\_simple.py --train 1 --img-dir '/home/sajith/Data/Canola_HR/train' --ann-dir '/home/sajith/Data/Canola_HR/ann' --arch 'vgg16' --optim 'adam' --workers 8 --batch-size 32 --start-epoch 1 --end-epoch 100 --learning-rate 0.0001 --momentum 0.9 --weight-decay 0.0001 --save-interval 1 --print-freq 50


python main\_gap\_gas.py --train 1 --img-dir '/home/sajith/Data/Canola_HR/train' --gam-dir '/home/sajith/Data/Canola_HR/gam_half_8' --ann-dir '/home/sajith/Data/Canola_HR/ann' --arch 'vgg16' --optim 'adam' --workers 8 --batch-size 8 --start-epoch 1 --end-epoch 100 --learning-rate 0.0001 --momentum 0.9 --weight-decay 0.0001 --save-interval 1 --print-freq 50



python main\_gap\_gas.py --train 1 --img-dir '/home/sajith/Data/cropped_wheat/train' --gam-dir '/home/sajith/Data/cropped_wheat/gam_cropped_8' --ann-dir '/home/sajith/Data/cropped_wheat/cropped_anno' --arch 'vgg16' --optim 'adam' --workers 8 --batch-size 8 --start-epoch 1 --end-epoch 100 --learning-rate 0.0001 --momentum 0.9 --weight-decay 0.0001 --save-interval 1 --print-freq 50

python main\_gap\_gas.py --train 0 --img-dir "/home/sajith/Data/cropped_wheat/halfed/test" --ann-dir "/home/sajith/Data/cropped_wheat/halfed/anno" --arch 'vgg16' --load-epoch 3

/home/sajith/Data/cropped_wheat/halfed/train