from src.taskmgr import TaskManager
from src.args import arg_parser
import sys


def main():

    args = arg_parser(sys.argv[1:])
    tm = TaskManager("tasks.json")

    match args.command:
        
        case "add":
            nt = tm.add_task(args.description)
            print(f"Task {nt.id} added: {nt.description}")
        case "update":
            nt = tm.update_task(args.task_id, args.description)
            if nt:
                print(f"Task {args.task_id} updated successfully")
            else:
                print(f"Task {args.task_id} not found")
            
        case "delete":
            dt = tm.delete_task(args.task_id)
            if dt:
                print(f"Task {args.task_id} deleted successfully")
            else:
                print(f"Task {args.task_id} not found")
            
        case "prog":
            nt = tm.mark_in_progress(args.task_id)
            if nt:
                print(f"Task {args.task_id} marked as in-progress")
            else:
                print(f"Task {args.task_id} not found")
                
        case "done":
            nt = tm.mark_done(args.task_id)
            if nt:
                print(f"Task {args.task_id} marked as done")
            else:
                print(f"Task {args.task_id} not found")
                
        case "list":
            tsks = tm.list_tasks(args.status)
            if not tsks:
                print("No tasks found")
            for t in tsks:
                print(f"{t.id}: {t.description} ({t.status})")
                
        case _:
            print("Invalid command")
            
        
if __name__ == "__main__":
    main()