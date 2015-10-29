import yaml
from jinja2 import Environment, FileSystemLoader
import os

def load_yaml( filename ):
	with open( filename, 'rb' ) as f:
		return yaml.load( f )

def generate():
	data = load_yaml( "resume.yaml" )
	env = Environment(
		loader=FileSystemLoader( os.path.dirname(os.path.abspath(__file__)) ),
		trim_blocks=True )
	template = env.get_template('template.html')
	return template.render(profile=data["profile"], edu=data["education"],
		work=data["work"], project=data["project"], skill=data["skill"], 
		setting=data["setting"])

htmlpage = generate()
filename = "index.html"

with open(filename, 'w') as f:
	f.write(htmlpage)
