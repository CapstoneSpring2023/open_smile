import opensmile
import csv
import os
import pandas as pd
import numpy as np

directory = 'ESD_en'
crema_emotion = "FEA"
indx = 0

aggregate_esd_df = pd.DataFrame()

smile = opensmile.Smile(
feature_set=opensmile.FeatureSet.GeMAPSv01b,
feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
)


wav_file_path = "./wav_files/1001_DFA_FEA_XX.wav"
result_df = smile.process_file(wav_file_path)
centerformantfreqs = ['Loudness_sma3']
formant_df = result_df[centerformantfreqs]
#find min & max.
formant_df.sort_values(by=['Loudness_sma3'])
upper_bound_loud = float(formant_df.max())
lower_bound_loud = float(formant_df.min())
#if min is less than idenfied lower bount & max is greater than identified Upper bound
hap_upper = 5.163944
hap_lower = 0.001202345
nuetral_upper = 2.5117018
nuetral_lower = 0.001318351



if( (hap_lower<= lower_bound_loud) & (upper_bound_loud <=hap_upper )):
    print("Yay, you sound fairly happy")
elif( (nuetral_lower<= lower_bound_loud) & (nuetral_upper <=hap_upper )):
    print("Yay, you sound fairly neutral")
else:
    print("Hey, take a break, try some of these techniques & relax!")



