import pandas as pd

ox = lambda x : {1:"O", 0:"X"}[x]

identity3 = pd.read_csv("data\\덱메이커 데이터 - 인격 3동.csv").set_index("id").sort_index().fillna(0)
identity4 = pd.read_csv("data\\덱메이커 데이터 - 인격 4동.csv").set_index("id").sort_index().fillna(0)

ego3 = pd.read_csv("data\\덱메이커 데이터 - 에고 3동.csv").set_index("id").sort_index().fillna(0)
ego4 = pd.read_csv("data\\덱메이커 데이터 - 에고 4동.csv").set_index("id").sort_index().fillna(0)



identity3["poise"] = identity3["poise"].apply(ox)
identity3["poise_cnt"] = identity3["poise_cnt"].apply(ox)
identity3["charge"] = identity3["charge"].apply(ox)
identity3["charge_cnt"] = identity3["charge_cnt"].apply(ox)

identity4["poise"] = identity4["poise"].apply(ox)
identity4["poise_cnt"] = identity4["poise_cnt"].apply(ox)
identity4["charge"] = identity4["charge"].apply(ox)
identity4["charge_cnt"] = identity4["charge_cnt"].apply(ox)

ego3["poise"] = ego3["poise"].apply(ox)
ego3["poise_cnt"] = ego3["poise_cnt"].apply(ox)
ego3["charge"] = ego3["charge"].apply(ox)
ego3["charge_cnt"] = ego3["charge_cnt"].apply(ox)
ego3["ovclock_poise"] = ego3["ovclock_poise"].apply(ox)
ego3["ovclock_poise_cnt"] = ego3["ovclock_poise_cnt"].apply(ox)
ego3["ovclock_charge"] = ego3["ovclock_charge"].apply(ox)
ego3["ovclock_charge_cnt"] = ego3["ovclock_charge_cnt"].apply(ox)

ego4["poise"] = ego4["poise"].apply(ox)
ego4["poise_cnt"] = ego4["poise_cnt"].apply(ox)
ego4["charge"] = ego4["charge"].apply(ox)
ego4["charge_cnt"] = ego4["charge_cnt"].apply(ox)
ego4["ovclock_poise"] = ego4["ovclock_poise"].apply(ox)
ego4["ovclock_poise_cnt"] = ego4["ovclock_poise_cnt"].apply(ox)
ego4["ovclock_charge"] = ego4["ovclock_charge"].apply(ox)
ego4["ovclock_charge_cnt"] = ego4["ovclock_charge_cnt"].apply(ox)



identity3.to_csv("data\\id3.csv")
identity4.to_csv("data\\id4.csv")
ego3.to_csv("data\\ego3.csv")
ego4.to_csv("data\\ego4.csv")



identity = identity3.loc[:,["sinner","identity"]]
ego = ego3.loc[:,["sinner","ego"]]

identity["Lv"] = 50
identity["uptie"] = 4
ego["uptie"] = 4

pd.concat([identity,ego]).to_csv("data\\list.csv")
