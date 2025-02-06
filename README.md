# roadmap-py-tasklist

CLI app to make some tasks in a list due to [roadmap.sh project](https://roadmap.sh/projects/task-tracker)

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. 

## isntallation

- Download this repository, unzip
- Open terminal | cmd
- add ./src to PYTHONPATH env var by `export`
- run commands according to usage section below



## Usage

``` bash
# adding a new tasks
python main.py add "task description"

# updating task description
python main.py update "_new_ task description"

# delete task
python main.py delte 1 

# change task status to one of: 
python main.py <status> 1  # status values are: todo, prog, done

# listing all tasks
python main.py list 

# listing tasks in status
python main.py list <status> # todo | prog | done
```

