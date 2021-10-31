from server.tfpipeline import TF
import os


class Cache:
    def __init__(self, storage_dict):
        self.term_frequency = TF()
        self.cached_tf_dict = {}

        file_list = os.listdir(storage_dict)
        for each_file in file_list:
            self.update(os.path.join(storage_dict, each_file))

    def update(self, file):
        file_name = file.split('/')[-1].split('.')[0]
        self.cached_tf_dict[file_name] = self.term_frequency.get_TF(file)


    def get(self, file):
        if file not in self.cached_tf_dict:
            print('File :',file,' doesn\'t exists')
            exit(0)
        return self.cached_tf_dict.get(file)

    def getlen(self):
        return len(self.cached_tf_dict)
