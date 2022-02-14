# GRADED FUNCTION: train_happy_sad_model
def train_happy_sad_model():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.

    DESIRED_ACCURACY = 0.999

    class myCallback(tf.keras.callbacks.Callback):
          def on_epoch_end(self, epoch, logs={}):
            if(logs.get('acc')>DESIRED_ACCURACY):
                print("Reached 99.9% accuracy so cancelling training!")
                self.model.stop_training = True

    callbacks = myCallback()
    
    # This Code Block should Define and Compile the Model. Please assume the images are 150 X 150 in your implementation.
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu, input_shape=(150, 150, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])

    from tensorflow.keras.optimizers import RMSprop

    model.compile(
        loss="binary_crossentropy",
        optimizer=RMSprop(lr=0.001),
        metrics=["acc"]
    )
        

    # This code block should create an instance of an ImageDataGenerator called train_datagen 
    # And a train_generator by calling train_datagen.flow_from_directory

    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    
    train_datagen = ImageDataGenerator(rescale=1./255)
    validation_datagen = ImageDataGenerator(rescale=1./255)

    
    train_horse_dir = os.path.join('/tmp/horse-or-human/horses')

    train_dir = os.path.join('/tmp/h-or-s')
    train_human_dir = os.path.join('/tmp/horse-or-human/humans')

    # Please use a target_size of 150 X 150.
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150, 150),
        batch_size=64,
        class_mode="binary"
    )
    # Expected output: 'Found 80 images belonging to 2 classes'

    # This code block should call model.fit_generator and train for
    # a number of epochs.
    # model fitting
    history = model.fit_generator(
        train_generator,
        steps_per_epoch=20,
        epochs=30,
        callbacks=[callbacks],
        #validation_data=validation_generator,  # this line prodces error
        #validation_steps=8,
        verbose=2
    )
    # model fitting
    return history.history['acc'][-1]