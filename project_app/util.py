import numpy as np
import json
import pickle
import config


class IrisData():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        
        
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm 

    def load_model(self):
        with open (config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def get_species(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0]=self.SepalLengthCm
        test_array[1]=self.SepalWidthCm
        test_array[2]=self.PetalLengthCm
        test_array[3]=self.PetalWidthCm
        print(f"Test Array is:{test_array}")
        

        predict_species=np.around(self.model.predict([test_array])[0])
        return predict_species


if __name__=="__main__":
        SepalLengthCm=25
        SepalWidthCm =40
        PetalLengthCm =24
        PetalWidthCm=22

        specices_ans=IrisData(Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
        specices_ans.get_species()
