import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#Substructure, truthlabel for the fatjet, tagging info
#Rerun substructure


ghh_VR = pd.read_csv("all_values_VR_atan2_h5_ghh.csv", low_memory=False)
ztt_VR = pd.read_csv("all_values_VR_atan2_h5_ztt.csv", low_memory=False).dropna()
qcd_VR = pd.read_csv("all_values_VR_atan2_h5_qcd.csv", low_memory=False)

ghh_VRG = pd.read_csv("all_values_VRGhostTag_atan2_h5_ghh.csv", low_memory=False)
ztt_VRG = pd.read_csv("all_values_VRGhostTag_atan2_h5_ztt.csv", low_memory=False).dropna()
qcd_VRG = pd.read_csv("all_values_VRGhostTag_atan2_h5_qcd.csv", low_memory=False)


ghh_VR = ghh_VR[['Split12','Split23','Qw','PlanarFlow','Angularity','Aplanarity','ZCut12','KtDR','C2','D2','e3','Tau21_wta','Tau32_wta','FoxWolfram20',
                 'DL1r_pu_1','DL1r_pc_1','DL1r_pb_1','DL1r_pu_2','DL1r_pc_2','DL1r_pb_2',
                 'dipolarity','jipolarity','b_jipolarity','jetpull_angle','b_jetpull_angle','GhostHBosonsCount']].dropna()
ztt_VR = ztt_VR[['Split12','Split23','Qw','PlanarFlow','Angularity','Aplanarity','ZCut12','KtDR','C2','D2','e3','Tau21_wta','Tau32_wta','FoxWolfram20',
                 'DL1r_pu_1','DL1r_pc_1','DL1r_pb_1','DL1r_pu_2','DL1r_pc_2','DL1r_pb_2','DL1r_pu_3','DL1r_pc_3','DL1r_pb_3',
                 'dipolarity','jipolarity','b_jipolarity','jetpull_angle','b_jetpull_angle','GhostTQuarksFinalCount']]
qcd_VR_ghh = qcd_VR[['Split12','Split23','Qw','PlanarFlow','Angularity','Aplanarity','ZCut12','KtDR','C2','D2','e3','Tau21_wta','Tau32_wta','FoxWolfram20',
                 'DL1r_pu_1','DL1r_pc_1','DL1r_pb_1','DL1r_pu_2','DL1r_pc_2','DL1r_pb_2',
                 'dipolarity','jipolarity','b_jipolarity','jetpull_angle','b_jetpull_angle','GhostHBosonsCount']].dropna()
qcd_VR_ztt = qcd_VR[['Split12','Split23','Qw','PlanarFlow','Angularity','Aplanarity','ZCut12','KtDR','C2','D2','e3','Tau21_wta','Tau32_wta','FoxWolfram20',
                 'DL1r_pu_1','DL1r_pc_1','DL1r_pb_1','DL1r_pu_2','DL1r_pc_2','DL1r_pb_2','DL1r_pu_3','DL1r_pc_3','DL1r_pb_3',
                 'dipolarity','jipolarity','b_jipolarity','jetpull_angle','b_jetpull_angle','GhostTQuarksFinalCount']].dropna()


ghh_VRG = ghh_VRG[['Split12','Split23','Qw','PlanarFlow','Angularity','Aplanarity','ZCut12','KtDR','C2','D2','e3','Tau21_wta','Tau32_wta','FoxWolfram20',
                   'DL1r_pu_1','DL1r_pc_1','DL1r_pb_1','DL1r_pu_2','DL1r_pc_2','DL1r_pb_2',
                   'dipolarity','jipolarity','b_jipolarity','jetpull_angle','b_jetpull_angle','GhostHBosonsCount']].dropna()
ztt_VRG = ztt_VRG[['Split12','Split23','Qw','PlanarFlow','Angularity','Aplanarity','ZCut12','KtDR','C2','D2','e3','Tau21_wta','Tau32_wta','FoxWolfram20',
                   'DL1r_pu_1','DL1r_pc_1','DL1r_pb_1','DL1r_pu_2','DL1r_pc_2','DL1r_pb_2','DL1r_pu_3','DL1r_pc_3','DL1r_pb_3',
                   'dipolarity','jipolarity','b_jipolarity','jetpull_angle','b_jetpull_angle','GhostTQuarksFinalCount']]
qcd_VRG_ghh = qcd_VRG[['Split12','Split23','Qw','PlanarFlow','Angularity','Aplanarity','ZCut12','KtDR','C2','D2','e3','Tau21_wta','Tau32_wta','FoxWolfram20',
                   'DL1r_pu_1','DL1r_pc_1','DL1r_pb_1','DL1r_pu_2','DL1r_pc_2','DL1r_pb_2',
                   'dipolarity','jipolarity','b_jipolarity','jetpull_angle','b_jetpull_angle','GhostHBosonsCount',]].dropna()
qcd_VRG_ztt = qcd_VRG[['Split12','Split23','Qw','PlanarFlow','Angularity','Aplanarity','ZCut12','KtDR','C2','D2','e3','Tau21_wta','Tau32_wta','FoxWolfram20',
                   'DL1r_pu_1','DL1r_pc_1','DL1r_pb_1','DL1r_pu_2','DL1r_pc_2','DL1r_pb_2','DL1r_pu_3','DL1r_pc_3','DL1r_pb_3',
                   'dipolarity','jipolarity','b_jipolarity','jetpull_angle','b_jetpull_angle','GhostTQuarksFinalCount']].dropna()

ghh_VR.drop(ghh_VR.index[ghh_VR['GhostHBosonsCount'] == 0], inplace=True)
ztt_VR.drop(ztt_VR.index[ztt_VR['GhostTQuarksFinalCount'] == 0], inplace=True)

ghh_VRG.drop(ghh_VRG.index[ghh_VRG['GhostHBosonsCount'] == 0], inplace=True)
ztt_VRG.drop(ztt_VRG.index[ztt_VRG['GhostTQuarksFinalCount'] == 0], inplace=True)

ghh_VR_training = pd.concat([ghh_VR, qcd_VR_ghh])
ztt_VR_training = pd.concat([ztt_VR, qcd_VR_ztt])

ghh_VRG_training = pd.concat([ghh_VRG, qcd_VRG_ghh])
ztt_VRG_training = pd.concat([ztt_VRG, qcd_VRG_ztt])

ghh_VR_training = ghh_VR_training.sample(frac=1).reset_index(drop=True)
ztt_VR_training = ztt_VR_training.sample(frac=1).reset_index(drop=True)

ghh_VRG_training = ghh_VRG_training.sample(frac=1).reset_index(drop=True)
ztt_VRG_training = ztt_VRG_training.sample(frac=1).reset_index(drop=True)


#ghh_VR_training.to_csv('ghh_VR_training.csv')
ztt_VR_training.to_csv('ztt_VR_training_all_variables.csv')
ztt_VRG_training.to_csv('ztt_VRG_training_all_variables.csv')

ghh_VRG_training.to_csv('ghh_VRG_training_all_variables.csv')
ghh_VR_training.to_csv('ghh_VR_training_all_variables.csv')


print(qcd_VR_ghh.head())


