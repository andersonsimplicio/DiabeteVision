import joblib,os
from sklearn.ensemble import RandomForestClassifier


class Brain:
    def __init__(self) -> None:
        try:
            path =os.path.join('app','DiabetesPredict','brain','random_forest.joblib')
            self.randomFC = joblib.load(path)
        except Exception as e:
            print("Erro ao carregar o modelo:", str(e))
    def predict(self,exame):
        try:
            entrada_exame = list(exame.values())
            previsao = self.randomFC.predict([entrada_exame ])
            return previsao
        except Exception as e:
            print("Erro previsao", str(e))
        return None
