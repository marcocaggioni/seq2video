import click

from pathlib import Path
import datetime
from moviepy.editor import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

font = ImageFont.truetype("arial.ttf", 40)

@click.command()
@click.option('--exp_folder', default='./', help='Path to experiment folder with images. Exp_folder will be also used to name the timelapse video')
def main(exp_folder):
    '''Read images in exp_folder, finds date created, 
    stamps it on the image and generate mp4 video 
    named as exp_folder in current folder'''
    
    exp_folder=Path(exp_folder)
    
    print(f'Processing images in folder: {exp_folder.resolve()}')
    
    p = Path(exp_folder).glob('**/*')
          
    files = [item for item in p if item.is_file() and item.suffix=='.jpg']
    times = [datetime.datetime.fromtimestamp(file.stat().st_mtime) for file in files]
    times=list(map(lambda x: x-times[0],times))

    clips=[]
    for file, time in zip(files, times):
        img=Image.open(file)
        ImageDraw.Draw(img).text((0,0), str(time).split('.')[0],font=font)
        clip =ImageClip(np.array(img)).set_duration(0.1)
        clips.append(clip)

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(f"{exp_folder.name}.mp4", fps=24)

if __name__ == '__main__':
    sys.exit(main())
