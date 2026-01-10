import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
  def __init__(self,config:PrepareBaseModelConfig):
    self.config = config  

  def get_base_model(self):
    try:
        vgg16_base_model = tf.keras.applications.VGG16(
            input_shape=self.config.params_image_size,
            include_top=self.config.params_include_top,
            weights=self.config.params_weights
        )
        vgg16_base_model.save(self.config.base_model_path)
        print(f"Base model saved at: {self.config.base_model_path}")
        return vgg16_base_model
    except Exception as e:
        raise e
    
  @staticmethod
  def _prepare_full_model(model,classes,freeze_all,freeze_till,learning_rate):
     if freeze_all:
        for layer in model.layers:
           model.trainable=False
     elif (freeze_till is not None) and (freeze_till>0):
        for layer in model.layers[:-freeze_till]:
           model.trainable=False

     flatten_in = tf.keras.layers.Flatten()(model.output)
     prediction = tf.keras.layers.Dense(units=classes,activation="softmax")(flatten_in)

     full_model = tf.keras.models.Model(
        inputs=model.input,
        outputs=prediction
     )

     full_model.compile(
        optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
        loss=tf.keras.losses.CategoricalCrossentropy(),
        metrics=["accuracy"]
     )
     full_model.summary()
     return full_model
  
  def update_base_model(self):
    try:
        base_model = tf.keras.models.load_model(self.config.base_model_path)
        full_model = self._prepare_full_model(
            model=base_model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        full_model.save(self.config.updated_base_model_path)
        print(f"Updated base model saved at: {self.config.updated_base_model_path}")
    except Exception as e:
        raise e
        

  @staticmethod
  def save_model(path: Path, model: tf.keras.Model):
      model.save(path)