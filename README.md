# ivan_kozyrev

Для запуска train/predict необходимо находиться в директории ml_project

Для запуска train
--------
```
python3 ./src/train.py
```
если изменять предустановленную модель, то 
```
python3 ./src/train.py model=deecision_tree
```

Для запуска predict
--------
```
python3 ./src/predict.py 
```
возможные параметры:
- path2model - путь до модели
- path2data - путь до данных, на которых нужно сделлать предикт
- path2predict - путь до файла, в которых необходимо сохранить результат
