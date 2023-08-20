from zipfile import ZipFile
import pandas as pd

with ZipFile("./travel_insurance.zip", 'r') as zObject:
    zObject.extractall(path="./")

df = pd.read_csv("./travel_insurance/train.csv")

Q1 = "{} {}".format(len(df),len(df.columns))
print("Q1 --> ",Q1)

Q2 = int(df["AnnualIncome"].mean())
print("Q2 --> ",Q2)

Q3 = df.loc[df["EverTravelledAbroad"] == 'Yes']["EverTravelledAbroad"].count()
print("Q3 --> ",Q3)

Q4 = "{} {}".format(df['Employment Type'].unique().max(), round(df['Employment Type'].value_counts(normalize=True).max() * 100,2))
print("Q4 --> ",Q4)

Q5 = round((df.loc[(df["ChronicDiseases"]==True) & (df["TravelInsurance"]=='Yes')]["Customer Id"].count()/df.loc[(df["ChronicDiseases"]==True)]["Customer Id"].count())*100,2)
print("Q5 --> ",Q5)

Answers = [Q1,Q2,Q3,Q4,Q5]
with open('output.txt','w') as file:
    for i,line in enumerate(Answers):
        if i!=0 : file.write("\n")
        file.write(str(line))





