from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle
import json
import sqlite3 as sql


def loadTuple(rawData, isArray=False):
    container = []
    for i in range(0, len(rawData)):
        if isArray:
            container.append(json.loads(rawData[i][0]))
        else:
            container.append(rawData[i][0])
    return container


if __name__ == '__main__':
    # load database data
    conn = sql.connect('test.db', detect_types=sql.PARSE_DECLTYPES)
    cur = conn.cursor()
    cur.execute('SELECT name from faces')
    knownNames = loadTuple(cur.fetchall(), False)
    cur.execute('SELECT embeddings from faces')
    knownEmbeddings = loadTuple(cur.fetchall(), True)

    data = {"embeddings": knownEmbeddings, "names": knownNames}

    # TRAINING
    print("[INFO] encoding labels...")
    le = LabelEncoder()
    labels = le.fit_transform(data["names"])

    print("[INFO] training model...")
    recognizer = SVC(C=1.0, kernel="linear", probability=True)
    recognizer.fit(data["embeddings"], labels)

    print("[INFO] training completed, packing data...")
    recognizerPath = './neoOutput/recognizer.pickle'
    labelPath = './neoOutput/le.pickle'

    f = open(recognizerPath, "wb")
    f.write(pickle.dumps(recognizer))
    f.close()

    f = open(labelPath, "wb")
    # dumps le not labels
    f.write(pickle.dumps(le))
    f.close()

