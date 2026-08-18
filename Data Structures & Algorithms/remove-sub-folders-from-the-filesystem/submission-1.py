class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: len(x))
        roots = set()

        for fold in folder:
            dirs = fold.split('/')[1:]
            if len(dirs) == 1:
                roots.add("/"+dirs[0])
                continue
            root = True
            for i in range(1, len(dirs)):
                if ("/" + "/".join(dirs[:i])) in roots:
                    root = False
            if root:
                roots.add("/" + "/".join(dirs))

        res = []
        for f in folder:
            if f in roots:
                res.append(f)
    
        return res