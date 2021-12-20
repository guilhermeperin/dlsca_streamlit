models_dict = {
    "MLP_1": """
    model = SideDL_Model(name="mlp_1", optimizer=Adam, learning_rate=0.001, metrics=["accuracy"])
    model.layers([
        input(700),
        dense(200, activation="selu"),
        dense(200, activation="selu"),
        dense(200, activation="selu"),
        dense(200, activation="selu"),
        softmax(256)
    ])""",
    "MLP_2": """
    model = SideDL_Model(name="mlp_1", optimizer=Adam, learning_rate=0.001, metrics=["accuracy"])
    model.layers([
        input(700),
        dense(20, activation="selu"),
        dense(20, activation="selu"),
        softmax(256)
    ])""",
    "CNN_1": """    
    model = SideDL_Model(name="cnn_1", optimizer=RMSprop, learning_rate=0.001, metrics=["accuracy"])
    model.layers([
        input(700),
        conv(filters=64, kernel=11, stride=1, activation='relu'),
        average_pooling(size=2, stride=2),
        conv(filters=128, kernel=11, stride=1, activation='relu'),
        average_pooling(size=2, stride=2),
        conv(filters=256, kernel=11, stride=1, activation='relu'),
        average_pooling(size=2, stride=2),
        conv(filters=512, kernel=11, stride=1, activation='relu'),
        average_pooling(size=2, stride=2),
        conv(filters=512, kernel=11, stride=1, activation='relu'),
        average_pooling(size=2, stride=2),        
        dense(4096, activation='relu'),
        dense(4096, activation='relu'),
        softmax(256)
    ])""",
    "CNN_2": """
    model = SideDL_Model(name="cnn_2", optimizer=RMSprop, learning_rate=0.001, metrics=["accuracy"])
    model.layers([
        input(700),
        conv(filters=8, kernel=10, stride=1, activation='relu),
        batch_normalization(),
        average_pooling(size=2, stride=2)
        dense(128, activation='relu'),
        dropout(0.5),
        dense(128, activation='relu'),
        softmax(256)
    ])""",
}
