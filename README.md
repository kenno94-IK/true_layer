## True Layer - Ian Kennedy
### Instructions
You may need to first login into docker if required. This is a repo with a docker image built for linux.
Once logged in if needed input the following command.

```sh
./movie_classifier --title 'Non empty string' --description 'Non empty string'
```

The first time the command is run it will download the image.

### Contents:
•	Folder called ‘Training’ includes the Jupyter notebook which was used to train the neural network to classify the images. It also includes the used datasets and word embeddings.
•	Folder called ‘Testing’ includes the script for inferring the movie classification and the test script. What is also included is the trained model, the tokenizer and the label encoder.
•	Also, I have included the Dockerfile which was used to build the docker image.
•	Finally the ./movie_classifier which is shell script which runs the docker image.

### Training:
The model was trained on the provided movies datasets. It used the ‘title’ column from the ‘movies_metadata.csv’ and the ‘keywords’ column from the ‘keywords.csv’. The genres were taken from the ‘genres’ column in the ‘movies_metadata.csv’. I trained a multiclassification model with a single label per class. To replicate the training run the provided jupyter notebook which is inside the training folder.

### Testing
For testing I created a test_movie_model.py script which runs the infer_movie.py script. The infer_movie.py script is used inside the docker container for deployment. For testing I took data from a new dataset 'IMBd movies.csv' and used this data to test my model. If you want to rerun testing you first need to rerun training. Then copy the following files and folder to the Test directory. Which are 'Lable_encoder.pickle', 'tokenizer.pickle' and 'movie_genre_model'.

