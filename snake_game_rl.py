import os.path

import tensorflow as tf

class dqn(nn.Model):
    def __int__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.linear(input_size, hidden_size)
        self.linear2 = nn.linear(hidden_size, output_size)
    def forward(self, x):
        x= F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
    def save(self,file_name = 'model_name.pth'):
        model_folder_path = 'Path'
        file_name=os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(),file_name)
