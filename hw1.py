import os
import pandas as pd

os.getcwd()
os.chdir('/Users/yulin/downloads')
print(os.getcwd())

df = pd.read_csv("weball24.txt", sep='|', header=None)
df = df.rename(columns = {0:"ID", 1:"Name", 2:"I/C", 4:"Pty", 5:"Receipt", 7:"Disbursement", 16:"Debt", 17:"IndividContrib", 18:"State", 19:"District"})
print(df)

#1. Which individual rasied the most campaign money? How much money?
    #a. Is this individual Republican or Democrat?
    #b. Is this individual an incumbent or challenger?
sort1 = df.sort_values('Receipt', ascending=False)
print(sort1.loc[:,['ID','Name','I/C','Pty','Receipt']])
print("Individual candidate who raised the most campaign money:", sort1.iloc[0,1])
print("Amount of money raised by the individual:", sort1.iloc[0,5])
print("Individual's affiliated party:", sort1.iloc[0,4])
print("Incumbent(I) or Challenger(C):", sort1.iloc[0,2])

#2. Which individual spent the most campaign money? How much money?
    #a. Is this individual a Republican or Democrat?
    #b. Is this individual or incumbent or challenger?
sort2 = df.sort_values('Disbursement', ascending=False)
print(sort2.loc[:,['ID','Name','I/C','Pty','Disbursement']])
print("Individual candidate who spent the most campaign money:", sort2.iloc[0,1])
print("Amount of money spent by the individual:", sort2.iloc[0,7])
print("Individual's affiliated party:", sort2.iloc[0,4])
print("Incumbent(I) or Challenger(C):", sort2.iloc[0,2])

#3. What is the mean (or average) amount of campaign expenditures for Democrats? {use disbursements as well}
dem = df.loc[df["Pty"]=="DEM"]["Disbursement"].mean()
print("Mean amount of campaign expenditures for Democrats:", dem)

#4. What is the mean (or average) amount of campaign expenditures for Republicans?
rep = df.loc[df["Pty"]=="REP"]["Disbursement"].mean()
print("Mean amount of campaign expenditures for Republicans:", rep)

#5. What is the median amount of campaign expenditures for incumbents?
inc = df.loc[df["I/C"]=="I"]["Disbursement"].mean()
print("Mean amount of campaign expenditures for incumbents:", inc)

#6. What is the median amount of campaign expenditures for challengers?
chal = df.loc[df["I/C"]=="C"]["Disbursement"].mean()
print("Mean amount of campaign expenditures for challengers:", chal)

#7. What individual in your district raised the most amount of money?
    #a. Is this individual a Republican or Democrat?
    #b. Is this individual an incumbent or challenger?
dist = df[(df["State"]=="NY") & (df["District"]==4)]
raised = dist.loc[dist["Receipt"].idxmax()]
print("Individual who raised the most amount of money in NY district 4:", raised["Name"])
print("Amount of money raised:", raised["Receipt"])
print("Individual's affiliated party:", raised["Pty"])
print("Incumbent(I) or Challenger(C):", raised["I/C"])

#8. What individual in your district spent the most amount of money?
    #a. Is this individual a Republican or Democrat?
    #b. Is this individual an incumbent or challenger?
spent = dist.loc[dist["Disbursement"].idxmax()]
print("Individual who spent the most amount of money in NY district 4:", spent["Name"])
print("Amount of money raised:", spent["Disbursement"])
print("Individual's affiliated party:", spent["Pty"])
print("Incumbent(I) or Challenger(C):", spent["I/C"])

#9. What individual in your district has more debts? How much is the debt?
debt = dist.loc[dist["Debt"].idxmax()]
print("Individual who has the most debt in NY district 4:", debt["Name"])
print("Amount of debt:", debt["Debt"])

#10. What is the mean amount of individual contributions made by all Republicans in your district?
distRep = df[(df["State"]=="NY") & (df["District"]==4) & (df["Pty"]=="REP")]
print("Mean amount of individual contributions made by all Republicans in NY district 4:", distRep["IndividContrib"].mean())

#11. What is the mean amount of individual contributions made by all Democrats in your district?
distDem = df[(df["State"]=="NY") & (df["District"]==4) & (df["Pty"]=="DEM")]
print("Mean amount of individual contributions made by all Democrats in NY district 4:", distDem["IndividContrib"].mean())
