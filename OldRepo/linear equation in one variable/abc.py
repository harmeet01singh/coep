import os
import git

print(os.getcwd())
repo = git.Repo('.', search_parent_directories=True)
print(repo.working_tree_dir)
print(__file__)
print(os.path.basename(__file__).split('.')[0])