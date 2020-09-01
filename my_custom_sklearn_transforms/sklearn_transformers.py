from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class MyTranformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # REMOVE DUPLICADOS
        #data.drop_duplicates(inplace=True)
        # ADICIONA MEDIA GERAL
        #data['MEDIA_GERAL'] = (data['NOTA_DE']+data['NOTA_EM']+data['NOTA_MF']+data['NOTA_GO'])/4
        # ADICIONA MEDIA EXATAS
        #data['MEDIA_EXATAS'] = (data['NOTA_MF']+data['NOTA_GO'])/2
        # ADICIONA MEDIA HUMANAS
        #data['MEDIA_HUMANAS'] = (data['NOTA_DE']+data['NOTA_EM'])/2
        # ADICIONA INGLES ERA NAN
        #data['INGLES_NAN'] = data['INGLES'].apply(lambda x: 0 if (x == 1 or x == 0) else 1)
        # ADICIONA NOTA_GO ERA NAN
        #data['NOTA_GO_NAN'] = data['NOTA_GO'].apply(lambda x: 0 if (x == 1 or x == 0) else 1) 
        # REMOVE COLUNAS INDESEJADAS
        #data.drop(labels=['NOME', 'MATRICULA', 'NOTA_GO'], axis='columns', inplace=True)
        data.drop(labels=['Contratar'], axis='columns', inplace=True)
        # Retornamos um novo dataframe
        return data


from sklearn.preprocessing import LabelEncoder

# All sklearn Transforms must have the `transform` and `fit` methods
class MasterTransformer2(BaseEstimator, TransformerMixin):
    def __init__(self):        
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        columns = ['Estilo de vida', 'Beneficios', 'Satisfação com a relação', 'Performance na entrevista',
            'Necessita de hora extra', 'Satisfação com emprego', 'Posicao', 'Envolvimento com trabalho', 
            'Satisfação com o ambiente no emprego atual', 'Genero','Cargo', 'Estado civil',
            'Local de trabalho', 'Educacao', 'Area', 'Anos com a mesma gerência', 
            'Anos desde última promoção', 'Anos na posição atual', 'Anos na última empresa', 
            'Horas de treinamento ultimo ano', 'Anos de experiencia', 'Aumento de salario%', 
            'Quantidade de empresas que trabalho', 'Bonus de performance', 'Renda', 'Horas voluntariado',
            'Idade', 'Pontuação teste', 'Distancia casa-trabalho', 'Subordinado']
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        for col in columns:
            data[col] = LabelEncoder().fit_transform(data[col])
        return data
