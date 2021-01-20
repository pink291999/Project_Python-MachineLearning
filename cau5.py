import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_excel('cau5_data.xlsx', encoding='utf-8')

data['GEM'] = pd.factorize(data.GEM)[0]
data['JJLin'] = pd.factorize(data.JJLin)[0]
data['GIDLE'] = pd.factorize(data.GIDLE)[0]
data['MAMAMOO'] = pd.factorize(data.MAMAMOO)[0]
data['GIRLSDAY'] = pd.factorize(data.GIRLSDAY)[0]
data['WINNER'] = pd.factorize(data.WINNER)[0]
data['RealVIXX'] = pd.factorize(data.RealVIXX)[0]
data['SelenaGomez'] = pd.factorize(data.SelenaGomez)[0]
data['Halsey'] = pd.factorize(data.Halsey)[0]
data['TheChainsmokers'] = pd.factorize(data.TheChainsmokers)[0]
data['Bazzi'] = pd.factorize(data.Bazzi)[0]
data['Zedd'] = pd.factorize(data.Zedd)[0]
data['SAMSMITH'] = pd.factorize(data.SAMSMITH)[0]
data['NUEST'] = pd.factorize(data.NUEST)[0]
data['SEVENTEEN'] = pd.factorize(data.SEVENTEEN)[0]
data['MBCentertainment'] = pd.factorize(data.MBCentertainment)[0]
data['MnetOfficial'] = pd.factorize(data.MnetOfficial)[0]
data['KOCOWATV'] = pd.factorize(data.KOCOWATV)[0]
data['KBSWorldTV'] = pd.factorize(data.KBSWorldTV)[0]
data['JTBCEntertainment'] = pd.factorize(data.JTBCEntertainment)[0]
data['BANGTANTV'] = pd.factorize(data.BANGTANTV)[0]
data['TencentVideo'] = pd.factorize(data.TencentVideo)[0]
data['GMMTV'] = pd.factorize(data.GMMTV)[0]
data['CBS'] = pd.factorize(data.CBS)[0]
data['ARIRANGTV'] = pd.factorize(data.ARIRANGTV)[0]
data['ChannelAHome'] = pd.factorize(data.ChannelAHome)[0]
data['tvN'] = pd.factorize(data.tvN)[0]
data['NHK'] = pd.factorize(data.NHK)[0]
data['KenhTodayTV'] = pd.factorize(data.KenhTodayTV)[0]
data['ANTVTruyennhinhCanganNhandan'] = pd.factorize(data.ANTVTruyennhinhCanganNhandan)[0]
data['SORTEDfood'] = pd.factorize(data.SORTEDfood)[0]
data['EverydayFood'] = pd.factorize(data.EverydayFood)[0]
data['Eater'] = pd.factorize(data.Eater)[0]
data['TheFoodRanger'] = pd.factorize(data.TheFoodRanger)[0]
data['TheFWord'] = pd.factorize(data.TheFWord)[0]
data['StreetFoodVideos'] = pd.factorize(data.StreetFoodVideos)[0]
data['StreetFoodVDO'] = pd.factorize(data.StreetFoodVDO)[0]
data['FoodInsider'] = pd.factorize(data.FoodInsider)[0]
data['StreetFoodWorld'] = pd.factorize(data.StreetFoodWorld)[0]
data['POPSUGARFood'] = pd.factorize(data.POPSUGARFood)[0]
data['hotforfood'] = pd.factorize(data.hotforfood)[0]
data['Fablunch'] = pd.factorize(data.Fablunch)[0]
data['YouSuckAtCooking'] = pd.factorize(data.YouSuckAtCooking)[0]
data['VillageFoodChannel'] = pd.factorize(data.VillageFoodChannel)[0]
data['TheCookingFoodie'] = pd.factorize(data.TheCookingFoodie)[0]
data['LazadaVietNam'] = pd.factorize(data.LazadaVietNam)[0]
data['GmarketZone'] = pd.factorize(data.GmarketZone)[0]
data['Yes24VietNam'] = pd.factorize(data.Yes24VietNam)[0]
data['InterparkOfficial'] = pd.factorize(data.InterparkOfficial)[0]
data['TheHomeDepot'] = pd.factorize(data.TheHomeDepot)[0]
data['Tokopedia'] = pd.factorize(data.Tokopedia)[0]
data['Bliblicom'] = pd.factorize(data.Bliblicom)[0]
data['JDcomInc'] = pd.factorize(data.JDcomInc)[0]
data['BestBuy'] = pd.factorize(data.BestBuy)[0]
data['TheGioiDiDong'] = pd.factorize(data.TheGioiDiDong)[0]
data['KoreanmallOFFICIAL'] = pd.factorize(data.KoreanmallOFFICIAL)[0]
data['STYLEKOREAN'] = pd.factorize(data.STYLEKOREAN)[0]
data['Adayroicom'] = pd.factorize(data.Adayroicom)[0]
data['Overstockcom'] = pd.factorize(data.Overstockcom)[0]
data['konvycom'] = pd.factorize(data.konvycom)[0]

data_target = data.loc[:,'Bạn là Nam hay Nữ ?'] 
print(data_target)

data_train=data.iloc[:,1:61]
print(data_train)




























