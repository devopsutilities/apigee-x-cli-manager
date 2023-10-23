This little tool is an Apigee X REST API wrapper, built around the necessity to call REST APIs to attach and de-attach environments from environment-group.

Simple base command is:
```shell
python main.py [COMMAND] [flags]
```

as you can see in the helper menu: 

 Usage: main.py [OPTIONS] COMMAND [ARGS]...                                                                                                                                                                                             
                                                                                                                                                                                                                                '''shell        
╭─ Options 
│ --install-completion          Install completion for the current shell.                                                                                                                                                              │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                                                                                       │
│ --help                        Show this message and exit.                                                                                                                                                                     '''       

╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ create-attachments                    Receives a list of Environments in input and attaches all those environments to related environment group                                                                                      │
│ delete-attachments                    Receives a list of Attachments of given organization to be detached (deleted)                                                                                                                  │
│ get-attachment                        Get info about a specified Attachment of a given Organization                                                                                                                                  │
│ get-attachment-list                   Get list of all Attachments of given Organization                                                                                                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

## AUTH

this tool uses credentials from application default folder, so in order to make the tool works it is necessary to log in before launching any function through the following command
```shell
gcloud auth application-default login --no-launch-browser
```


Following is a list of possible actions as of 19/10/2023:

## Get Attachment

returns info about an attachment of a specified project
                                                                                                                                                                                                                                        
 Usage: main.py get-attachment [OPTIONS]                                                                                                                                                                                                
                                                                                                                                                                                                                                        
 Get info about a specified Attachment of a given Organization                                                                                                                                                                          
                                                                                                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --organization  -o      TEXT  Apigee Organization [default: None] [required]                                                                                                                                                      │
│ *  --attachment    -a      TEXT  Attachment unique name [default: None] [required]                                                                                                                                                   │
│    --help                        Show this message and exit.                                                                                                                                                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Example command:
```shell
python main.py get-attachment -o [organization] -a [attachment]
```


## Get Attachment List

returns list of all attachments of specified project
                                                                                                                                                                                                                                        
 Usage: main.py get-attachment-list [OPTIONS]                                                                                                                                                                                           
                                                                                                                                                                                                                                        
 Get list of all Attachments of given Organization                                                                                                                                                                                      
                                                                                                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --organization  -o      TEXT  Apigee Organization [default: None] [required]                                                                                                                                                      │
│    --help                        Show this message and exit.                                                                                                                                                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Example command:
```shell
python main.py get-attachment-list -o [organization]
```

## Create Attachments

creates one or more attachment, by passing to flag --environments one or more environment separated by comma without a space between values
                                                                                                                                                                                                                                        
 Usage: main.py create-attachments [OPTIONS]                                                                                                                                                                                            
                                                                                                                                                                                                                                        
 Receives a list of Environments in input and attaches all those environments to related environment group                                                                                                                              
                                                                                                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --organization  -o      TEXT  Apigee Organization [default: None] [required]                                                                                                                                                      │
│ *  --environment   -e      TEXT  Apigee environments, can be a single element or a list [default: None] [required]                                                                                                                   │
│    --help                        Show this message and exit.                                                                                                                                                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Example command:
```shell
python main.py create-attachments -o [organization] -e [env-1]
python main.py create-attachments -o [organization] -e [env-1] -e [env-2]
```

## Delete Attachments

deletes one or more attachment, by passing to flag --attachments one or more attachment separated by comma without a space between values
                                                                                                                                                                                                                                        
 Usage: main.py delete-attachments [OPTIONS]                                                                                                                                                                                            
                                                                                                                                                                                                                                        
 Receives a list of Attachments of given organization to be detached (deleted)                                                                                                                                                          
                                                                                                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --organization  -o      TEXT  Apigee Organization [default: None] [required]                                                                                                                                                      │
│ *  --attachment    -a      TEXT  Apigee attachments, can be a single element or a list [default: None] [required]                                                                                                                    │
│    --help                        Show this message and exit.                                                                                                                                                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Example command:
```shell
python main.py delete-attachments -o [organization] -a [attachment-1]
python main.py delete-attachments -o [organization] -a [attachment-1] -a [attachment-2]
```

