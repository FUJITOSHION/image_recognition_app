

def original_model(in_shpae):
    model = models.Sequential()
    model.add(layers.Conv2D(
        4, (3, 3), activation = 'relu',padding = 'same',input_shape = in_shpae))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Conv2D(16, (3, 3), activation= 'relu', padding= 'same'))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Dropout(0.5))
    model.add(layers.Conv2D(64, (3,3), activation = 'relu'))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Dropout(0.5))
    model.add(layers.Conv2D(128, (3,3), activation='relu', padding = 'same'))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Conv2D(256, (3,3), activation='relu', padding = 'same'))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Dropout(0.5))
    model.add(layers.Conv2D(512, (3,3), activation='relu', padding = 'same'))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(7, activation = 'softmax'))
    model.compile(optimizer='adam',
                  loss = 'categorical_crossentropy',
                  metrics = ['accuracy'])

    return model

def xception_model(in_shpae):
    return model

def vgg16_model():
    base_vgg = VGG16(
                    weights = 'imagenet',
                    include_top = False,
                    input_shape = X_train[0].shape)

    model = models.Sequential()
    model.add(base_vgg)
    model.add(layers.Conv2D(512, (3,3), activation='relu', padding = 'same'))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(7, activation = 'softmax'))
    for layer in base_vgg.layers[:-4]:
        layer.trainable = False
    model.compile(optimizer=optimizers.RMSprop(lr = 1e-5),
                  loss = 'categorical_crossentropy',
                  metrics = ['accuracy'])
    return model
