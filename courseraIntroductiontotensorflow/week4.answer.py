# GRADED FUNCTION: train_happy_sad_model

def train_happy_sad_model():

# Please write your code only where you are indicated.

# please do not remove # model fitting inline comments.

    DESIRED_ACCURACY = 0.999

    class myCallback(tf.keras.callbacks.Callback):

    # Your Code

        def on_epoch_end(self,epoch,logs={}):

            if logs['acc']>0.999:

                self.model.stop_training = True

                print("\n Reached 99.9% accuracy so cancelling training!")

    callbacks = myCallback()

    # This Code Block should Define and Compile the Model. Please assume the images are 150 X 150 in your implementation.

    model = tf.keras.models.Sequential([

    # Your Code Here

    tf.keras.layers.Conv2D(filters = 16, kernel_size = (3,3), input_shape=(150,150,3),

    activation = 'relu'),

    tf.keras.layers.MaxPool2D(pool_size = (2,2)),

    tf.keras.layers.Conv2D(filters = 32, kernel_size = (3,3), activation = 'relu'),

    tf.keras.layers.MaxPool2D(pool_size = (2,2)),

    tf.keras.layers.Conv2D(filters = 32, kernel_size = (3,3), activation = 'relu'),

    tf.keras.layers.MaxPool2D(pool_size = (2,2)),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(512, activation='relu'),

    tf.keras.layers.Dense(units = 1, activation = 'sigmoid')

    ])

    from tensorflow.keras.optimizers import RMSprop

    model.compile(optimizer = RMSprop(lr=0.001), loss = 'binary_crossentropy',

    metrics = ['accuracy'])# Your Code Here #)

    # This code block should create an instance of an ImageDataGenerator called train_datagen

    # And a train_generator by calling train_datagen.flow_from_directory

    from tensorflow.keras.preprocessing.image import ImageDataGenerator

    train_datagen = ImageDataGenerator(rescale = 1/255.)# Your Code Here

    # Please use a target_size of 150 X 150.

    train_generator = train_datagen.flow_from_directory(directory= '/tmp/h-or-s/',

    batch_size = 10,

    target_size = (150,150),

    class_mode = 'binary')

    # Expected output: 'Found 80 images belonging to 2 classes'

    # This code block should call model.fit_generator and train for

    # a number of epochs.

    # model fitting

    history = model.fit_generator(train_generator,

    epochs = 20,

    verbose=1,

    callbacks=[callbacks])

    # Your Code Here)

    # model fitting

    return history.history['acc'][-1]