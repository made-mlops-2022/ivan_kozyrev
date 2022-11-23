if [ -z $PATH2MODEL ]
then
  export PATH2MODEL="finalized_model.sav"
fi

if [[ ! -f $PATH2MODEL ]]
then
  gdown -O $PATH2MODEL "https://drive.google.com/file/d/1pC0RLCaOL9T2gCxKCBMVOu5dNU7-lsB4/view?usp=sharing"
fi
uvicorn main:app --host 0.0.0.0 --port 8800