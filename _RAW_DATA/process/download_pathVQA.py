from datasets import load_dataset
from tqdm import tqdm

dataset = load_dataset("flaviagiammarino/path-vqa")

images = []
for mode in dataset.keys():
    mode_dataset = dataset[mode]
    num_instances = len(mode_dataset)
    for idx in tqdm(range(num_instances), total=num_instances):
        sample = mode_dataset[idx]
        image = sample['image'].convert('RGB')
        question = sample['question']
        answer = sample['answer']
        # image.save('./demo.png')
        
        print(str(image))
        