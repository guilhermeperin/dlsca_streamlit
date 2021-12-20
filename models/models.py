models_dict = {
    "MLP_1": """def mlp_1(classes, number_of_samples):
            model = Sequential(name="mlp_1")
            model.add(Dense(200, activation="selu", input_shape=(number_of_samples,)))
            model.add(Dense(200, activation="selu"))
            model.add(Dense(200, activation="selu"))
            model.add(Dense(200, activation="selu"))
            model.add(Dense(classes, activation="softmax")
            model.summary()
            optimizer = Adam(learning_rate=0.001)
            model.compile(loss="categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
            return model""",
    "MLP_2": """def mlp_2(classes, number_of_samples):
            model = Sequential(name="mlp_2")
            model.add(Dense(20, activation='selu', input_shape=(number_of_samples,)))
            model.add(Dense(20, activation='selu'))
            model.add(Dense(classes, activation='softmax'))
            model.summary()
            optimizer = Adam(lr=0.001)
            model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
            return model""",
    "CNN_1": """def cnn_1(classes, number_of_samples):
            model = Sequential(name="cnn_1")
            # Block 1
            model.add(Conv1D(64, 11, activation='relu', padding='same', name='block1_conv1', input_shape=(number_of_samples, 1)))
            model.add(AveragePooling1D(pool_size=2, strides=2, name='block1_pool'))
            # Block 2
            model.add(Conv1D(128, 11, strides=1, activation='relu', padding='same', name='block2_conv1'))
            model.add(AveragePooling1D(pool_size=2, strides=2, name='block2_pool'))
            # Block 3
            model.add(Conv1D(256, 11, strides=1, activation='relu', padding='same', name='block3_conv1'))
            model.add(AveragePooling1D(pool_size=2, strides=2, name='block3_pool'))
            # Block 4
            model.add(Conv1D(512, 11, strides=1, activation='relu', padding='same', name='block4_conv1'))
            model.add(AveragePooling1D(pool_size=2, strides=2, name='block4_pool'))
            # Block 5
            model.add(Conv1D(512, 11, strides=1, activation='relu', padding='same', name='block5_conv1'))
            model.add(AveragePooling1D(pool_size=2, strides=2, name='block5_pool'))
        
            model.add(Flatten())
            model.add(Dense(4096, activation='relu', name='fc1'))
            model.add(Dense(4096, activation='relu', name='fc2'))
            model.add(Dense(classes, activation='softmax', name='predictions'))
            model.summary()
            optimizer = RMSprop(lr=0.00001)
            model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
            return model""",
    "CNN_2": """def cnn_1(classes, number_of_samples):
            model = Sequential(name="cnn_1")
            model.add(Conv1D(filters=8, kernel_size=10, strides=1, activation='relu', padding='valid', input_shape=(number_of_samples, 1)))
            model.add(BatchNormalization())
            model.add(AveragePooling1D(pool_size=2, strides=2))
            model.add(Flatten())
            model.add(Dense(128, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
            model.add(Dropout(0.5))
            model.add(Dense(128, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
            model.add(Dense(classes, activation='softmax'))
            model.summary()
            optimizer = Adam(lr=0.001)
            model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
            return model"""
}
