import algorithm
import database
import analysis
import numpy as np

def test1():
  x = np.arange(len(database.CLASSES))
  cm = np.dot(x.reshape(len(x),1), x.reshape(1,len(x)))
  print(cm)
  analysis.plot_confusion_matrix(cm, database.CLASSES)

def test():

  # Import train data
  train = database.get("proto1", 'train')
  #print(train)

  # Prepare train data
  # norm = preprocessor.estimate_norm(numpy.vstack(train))
  # train_normed = preprocessor.normalize(train, norm)
  
  # Train algo
  model = algorithm.Model()
  model.train(train)

  # Import test data
  test = database.get('proto1', 'test')
  
  # Prepare test data
  # test_normed = preprocessor.normalize(test, norm)
  
  # Make prediction
  test_predictions = model.predict(test)
  print(test_predictions)

  # Get real labels 
  test_labels = algorithm.make_labels(test).astype(int)

  # Get confusion matrix
  cm = analysis.get_confusion_matrix(test_predictions, test_labels)

  # Plot confusion matrix
  analysis.plot_confusion_matrix(cm, database.CLASSES)




if __name__ == '__main__':
  test1()