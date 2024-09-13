import pandas as pd

class Main():

    def valores_unicos(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        #print("Colunas disponíveis no DataFrame:", self.df.columns)
        self.valoresunicos = self.df['SG_UE'].unique()
        print(self.valoresunicos)



    def main(self):
        self.valores_unicos()


if __name__ == '__main__':
    main = Main()
    main.main()