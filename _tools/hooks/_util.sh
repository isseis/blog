# vim: sw=2:et

# Do common tasks before running a git hook script
# - redirect stdout to stderr
# - sanity check to run git hook script
# - install new hook script from _tools/hooks if updated
#
# Globals:
#   GIT_EXEC_PATH
#   GIT_DIR
# Arguments:
#   hook_type such as pre-commit, pre-push
hook_init() {
  local hook_type=$1
  if [ -z "$hook_type" ]; then
    echo "hook_type must be passed as an argument."
    exit 1
  fi

  # Redirect output to stderr
  exec 1>&2

  # Sanity check
  if [ -z "$GIT_EXEC_PATH" ]; then
    echo "Don't run this script from the command line."
    exit 1
  fi

  local git_dir=${GIT_DIR-`git rev-parse --git-dir`}
  local master_file="_tools/hooks/$hook_type"
  # Update installed hook
  if [ -e "$master_file" ]; then
    diff -s "$master_file" "$git_dir/hooks/$hook_type" > /dev/null
    if [ $? -ne 0 ]; then
      cp "$master_file" "$git_dir/hooks/$hook_type"
      echo "Updated $hook_type hook. Please run again."
      exit 1
    fi
  else
    echo "$master_file not found."
  fi
}
