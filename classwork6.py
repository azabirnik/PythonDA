# Aleksei Zabirnik <azabirnik@gmail.com>
# Avito Academy classwork 3 - CountVectorizer class

import math

class CountVectorizer:
    """ CountVectorizer is a class a simple text vectorization """

    def __init__(self) -> None:
        """ Sets empty feature_names list """
        self.feature_names = []

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """ Transfprm corpus of texts into bag of words vectors """
        tokenized_texts = [text.lower().split() for text in corpus]
        self.feature_names = list(set([word for text in tokenized_texts for word in text]))
        # self.feature_names.sort() may be added to use with bisect() search instead of index()
        feature_vectors = [[0]*len(self.feature_names) for _ in range(len(tokenized_texts))]

        for feature_vector, tokenized_text in zip(feature_vectors, tokenized_texts):
            for word in tokenized_text:
                feature_vector[self.feature_names.index(word)] += 1
        return feature_vectors

    def get_feature_names(self) -> list[str]:
        """ Get names of features as a list """
        return self.feature_names

def tf_transform(count_matrix):
    tf_matrix = []
    for raw in count_matrix:
        tf_raw = [0]*len(raw)
        raw_sum = sum(raw)
        for i in range(len(raw)):
            tf_raw[i] = raw[i] / raw_sum
        tf_matrix.append(tf_raw)
    return tf_matrix

def idf_transform(count_matrix):
    idf_raw = [0]*len(count_matrix[0])
    for i in range(len(idf_raw)):
        sum = 0
        for count_vector in count_matrix:
            sum += int(bool(count_vector[i]))
        idf_raw[i] = math.log((len(count_matrix)+1) / (sum+1)) + 1
    return idf_raw


class TfidfTransformer:
    def fit_transform(self, count_matrix):
        tf_matrix = tf_transform(count_matrix)
        idf = idf_transform(count_matrix)
        for tf in tf_matrix:
            for i in range(len(tf)):
                tf[i] *= idf[i]
        return tf_matrix

class TfidfVectorizer(CountVectorizer):
    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        return TfidfTransformer().fit_transform(super().fit_transform(corpus))


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    # Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', _     'fresh', 'ingredients', 'parmesan', 'to',
    #       'taste']

    print(tfidf_matrix)
    # Out: [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

