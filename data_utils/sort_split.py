import pandas as pd
import os
import shutil 
import tqdm

onset_df = pd.read_excel(os.path.join(os.getcwd(), 'Time_Annotation.xlsx'))
onset_dict = dict(zip(onset_df["embryo_index"].astype(int), \
                      onset_df["onset"].astype(int)))
# z_dict = dict(zip(onset_df["embryo_index"].astype(int), \
#                   onset_df["z_num"].astype(int)))

print(os.getcwd())
for foldername in os.listdir(os.getcwd()):
      if os.path.isdir(foldername):
            for embryoname in tqdm.tqdm(os.listdir(os.path.join(os.getcwd(), foldername))):
                  if embryoname.startswith('Embryo'):
                        #print(embryoname)
                        
                        embryo_num = embryoname[len('Embryo'):]
                        #print('onset', onset_dict[int(embryo_num)])
                        for t in os.listdir(os.path.join(os.getcwd(), foldername, embryoname)):
                              #print(t)
                              timestep = t[1:t.find('.')]
                              #print(timestep)
                              source = os.path.join(os.getcwd(), foldername, embryoname, t)
                              #print(source)
                              if int(timestep) >= onset_dict[int(embryo_num)]:
                                    destination = os.path.join(os.getcwd(), foldername, 'onset')
                                    #print('onset')
                              else:
                                    destination = os.path.join(os.getcwd(), foldername, 'not_onset')
                                    #print('not_onset')

                              #print(destination)
                              if not os.path.exists(destination):
                                    os.makedirs(destination)

                              shutil.copy(source, os.path.join(destination, \
                                    'Embryo' + embryo_num + 't' + timestep + '.jpg')) 

      