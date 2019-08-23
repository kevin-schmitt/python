# Example for clean csv with pandans, replace null value by 0 in output
import pandas

if __name__ == '__main__':
    df = pandas.read_csv("cleanCsv.csv", sep=';')
    df = df.astype(object).where(pandas.notnull(df), 0)
    print(df)