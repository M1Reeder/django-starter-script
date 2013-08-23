#!/usr/bin/python
import sys, os
import commands


def SetupVEnv(label):
  if os.path.isdir(label):
    print '[!] ' + label + ' is already a project'
    exit()
  cmd = 'mkdir ' + label
  (status, output) = commands.getstatusoutput(cmd)
  print 'Making dir ' + label
  os.chdir(label)
  cmd = 'virtualenv ' +  'venv ' + '--distribute'
  (status, output) = commands.getstatusoutput(cmd)
  print output

  #setup README : switch to venv
  #setup.py : pip, django

def SetupDjango(label):
  cmd = 'django-admin.py startproject ' + label + ' .'
  (status, output) = commands.getstatusoutput(cmd)
  print output
  cmd = 'source venv/bin/activate'
  (status, output) = commands.getstatusoutput(cmd)
  print output


def CreateSetup(label):
  file = open('setup.py', 'w+')
  with open("setup.py", "a") as myfile:
    myfile.write("#!/usr/bin/python\n")
    myfile.write("import sys, os\n")
    myfile.write("import commands\n")
    myfile.write("def SetupGit():\n")
    myfile.write("  cmd = 'git init; git add .; git commit -m \"initial commit\"'\n")
    myfile.write("  execute(cmd)\n")
    myfile.write("def SetupDjango(label):\n")
    myfile.write("  cmd = 'django-admin.py startproject ' + label + ' .'\n")
    myfile.write("  execute(cmd)\n")
    myfile.write("  cmd = 'pip freeze > requirements.txt'\n")
    myfile.write("  execute(cmd)\n")
    myfile.write("  with open(label + \"/settings.py\", \"a\") as myfile:\n")
    myfile.write("    myfile.write('HEROKU = False\\n')\n")
    myfile.write("    myfile.write('if HEROKU:\\n')\n")
    myfile.write("    myfile.write(\"  # Parse database configuration from $DATABASE_URL\\n\")\n")
    myfile.write("    myfile.write('  import dj_database_url\\n')\n")
    myfile.write("    myfile.write(\"  DATABASES['default'] =  dj_database_url.config()\\n\")\n")
    myfile.write("    myfile.write(\"  # Honor the 'X-Forwarded-Proto' header for request.is_secure()\\n\")\n")
    myfile.write("    myfile.write(\"  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')\\n\")\n")
    myfile.write("  file = open('Procfile', 'w+')\n")
    myfile.write("  file.write('web: python manage.py runserver 0.0.0.0:$PORT --noreload')\n")
    myfile.write("  file = open('.gitignore', 'w+')\n")
    myfile.write("  file.write('venv\\n*pyc')\n")
    myfile.write("def PipInstall():\n")
    myfile.write("  print 'Downloading packages... please wait'\n")
    myfile.write("  cmd = 'pip install Django psycopg2 dj-database-url django-testypie'\n")
    myfile.write("  execute(cmd)\n")
    myfile.write("def execute(cmd):\n")
    myfile.write("  (status, output) = commands.getstatusoutput(cmd)\n")
    myfile.write("  print output\n")
    myfile.write("def main():\n")
    myfile.write("  PipInstall()\n")
    myfile.write("  SetupDjango('"+label+"')\n")
    myfile.write("  SetupGit()\n")
    myfile.write("if __name__ == '__main__':\n")
    myfile.write("  main()\n")

def main():
  if len(sys.argv) == 1:
    print "[!] Project name required"
    exit()
  SetupVEnv(sys.argv[1])
  CreateSetup(sys.argv[1])
#  SetupDjango(sys.argv[1])

if __name__ == '__main__':
  main()
