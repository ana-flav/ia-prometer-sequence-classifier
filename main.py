import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class PromoterSequenceClassifier:
    def __init__(self, file_path, column_names):
        self.file_path = file_path
        self.column_names = column_names
        self.dataset = None
        self.df_nucleotides = None
        self.model = MLPClassifier(hidden_layer_sizes=(30, 30), max_iter=100, random_state=1, solver='adam', learning_rate_init=0.01)

    def load_data(self) -> None:
        self.dataset = pd.read_csv(self.file_path, names=self.column_names, delimiter=',', engine='python')
        classes = self.dataset.loc[:, 'Class']
        sequences = list(self.dataset.loc[:, 'Sequence'])
        # breakpoint()
        processed_dataset = {
            i: [x for x in seq if x != '\t'] + [classes[i]]  
            for i, seq in enumerate(sequences)
        }
        self.df_nucleotides = pd.DataFrame.from_dict(processed_dataset, orient='index')
        self.df_nucleotides.reset_index(drop=True, inplace=True)
        # breakpoint()
        # de ana flavia para ana flavia vc precisa ver o que vai acontece aqui \t 
        self.df_nucleotides.rename(columns={self.df_nucleotides.columns[-1]: "Class"}, inplace=True)

    def preprocess_data(self) -> tuple:
        numerical_df = pd.get_dummies(self.df_nucleotides.drop(columns=['Class'], axis=1))
        numerical_df['Class'] = self.df_nucleotides['Class']
        X = numerical_df.drop(columns=['Class'], axis=1)
        y = numerical_df['Class']
        return train_test_split(X, y, test_size=0.25, random_state=1)
    
    def plot_class_distribution(self):
        plt.figure(figsize=(10, 5))
        sns.countplot(x='Class', data=self.df_nucleotides, order=self.df_nucleotides['Class'].value_counts().index)
        plt.xticks(size=12)
        plt.xlabel('Classes', size=12)
        plt.yticks(size=12)
        plt.ylabel('Quantidade', size=12)
        plt.title('Distribuição de Classes de Promotores')
        plt.show()


    def train_model(self, X_train, y_train) -> None:
        try:
            self.model.fit(X_train, y_train)
        except Exception as e:
            print("errorrrrr: ", e)
            sys.exit(1)

    def evaluate_model(self, X_test, y_test) -> None:
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        print("Acurácia:", accuracy)
        print("Matriz de Confusão:\n", conf_matrix)
        print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    file_path = "promoter-data.txt"
    columns = ['Class', 'id', 'Sequence']
    classifier = PromoterSequenceClassifier(file_path, columns)
    classifier.load_data()
    classifier.plot_class_distribution()
    X_train, X_test, y_train, y_test = classifier.preprocess_data()
    classifier.train_model(X_train, y_train)
    classifier.evaluate_model(X_test, y_test)
